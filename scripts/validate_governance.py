#!/usr/bin/env python3
"""Fail-closed repository governance checks for GorkBot.

This validator intentionally checks only invariants that can be derived from the
committed repository. It does not replace task-specific author/challenger/
verifier evidence.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "venv",
}

LIST_STATUS_CLASSES = {
    "active_task_ids": "active",
    "ready_task_ids": "ready",
    "backlog_task_ids": "backlog",
    "completed_task_ids": "completed",
    "blocked_task_ids": "blocked",
}

SECRET_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "private key",
        re.compile(
            r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----"
        ),
    ),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{70,}\b")),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    (
        "OpenAI-style secret key",
        re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b"),
    ),
)

# All secret patterns are confined to one line, but some token lengths are
# unbounded. Read bounded lines so neither a huge file nor one huge line can
# exhaust memory; reject overlong lines rather than scan incomplete tokens.
SECRET_SCAN_LINE_LIMIT = 1_000_000

FORBIDDEN_TRACKED_NAMES = {
    ".env",
    "credentials.json",
}
FORBIDDEN_TRACKED_SUFFIXES = {
    ".key",
    ".p12",
    ".pem",
    ".pfx",
}

FROZEN_DIGEST_SOURCE = Path(
    "10_checkpoints/stage_checkpoints/"
    "ENGINEERING_PREVIEW_E2_ARCHITECTURE_VERIFICATION.yaml"
)
FROZEN_EXACT_PATHS = {
    "06_evaluation/ENGINEERING_PREVIEW_EVALUATION_SUITE.md",
    "06_evaluation/MODEL_ROLE_BENCHMARK_PLAN.md",
    "10_checkpoints/stage_checkpoints/"
    "ENGINEERING_PREVIEW_E1_SPECIFICATION_GATE_VERIFICATION.yaml",
}


class ValidationError(RuntimeError):
    """Raised when a repository invariant fails."""


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def _construct_unique_mapping(
    loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError as exc:
            raise ValidationError(
                f"Unhashable YAML mapping key at line {key_node.start_mark.line + 1}"
            ) from exc
        if duplicate:
            raise ValidationError(
                "Duplicate YAML key "
                f"{key!r} at line {key_node.start_mark.line + 1}"
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def repo_files(suffixes: Iterable[str] | None = None) -> list[Path]:
    wanted = set(suffixes or [])
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if wanted and path.suffix.lower() not in wanted:
            continue
        paths.append(path)
    return sorted(paths)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_yaml(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.load(handle, Loader=UniqueKeyLoader)
    except (OSError, UnicodeError, yaml.YAMLError, ValidationError) as exc:
        raise ValidationError(f"YAML validation failed for {rel(path)}: {exc}") from exc


def check_yaml() -> int:
    paths = repo_files({".yaml", ".yml"})
    for path in paths:
        load_yaml(path)
    return len(paths)


def check_csv() -> int:
    paths = repo_files({".csv"})
    for path in paths:
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                rows = [row for row in csv.reader(handle) if row]
        except (OSError, UnicodeError, csv.Error) as exc:
            raise ValidationError(f"CSV parse failed for {rel(path)}: {exc}") from exc
        if not rows:
            raise ValidationError(f"CSV file is empty: {rel(path)}")
        width = len(rows[0])
        if width == 0:
            raise ValidationError(f"CSV header is empty: {rel(path)}")
        for index, row in enumerate(rows[1:], start=2):
            if len(row) != width:
                raise ValidationError(
                    f"CSV width mismatch in {rel(path)} line {index}: "
                    f"expected {width}, got {len(row)}"
                )
    return len(paths)


def check_json() -> int:
    paths = repo_files({".json"})
    for path in paths:
        try:
            with path.open("r", encoding="utf-8") as handle:
                json.load(handle)
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise ValidationError(f"JSON parse failed for {rel(path)}: {exc}") from exc
    return len(paths)


def require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{label} must be a mapping")
    return value


def require_string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValidationError(f"{label} must be a list of strings")
    if len(value) != len(set(value)):
        raise ValidationError(f"{label} contains duplicate task IDs")
    return value


def status_class(status: Any) -> str:
    text = str(status or "").upper()
    if text == "READY":
        return "ready"
    # PROJECT_STATE's E3-002 qualification denotes completed Phase A protocol
    # work, not Phase B execution authority. Preserve that documented form,
    # but arbitrary VERIFIED_* strings cannot establish task completion.
    if text in {"VERIFIED", "VERIFIED_PHASE_A_PROTOCOL_CRITERIA_NOT_EXECUTION_READY"}:
        return "completed"
    if text == "BACKLOG" or text.startswith("BACKLOG_"):
        return "backlog"
    if text == "BLOCKED" or text.startswith("BLOCKED_"):
        return "blocked"
    if (
        text in {"ACTIVE", "CLAIMED", "IN_PROGRESS", "READY_FOR_REVIEW"}
        or text.startswith("ACTIVE_")
        or text.startswith("CLAIMED_")
        or text.startswith("IN_PROGRESS_")
        or text.startswith("READY_FOR_REVIEW_")
    ):
        return "active"
    raise ValidationError(f"Unrecognized task status: {status!r}")


def check_task_graph_and_state() -> tuple[int, int]:
    registry_path = ROOT / "01_governance/TASK_REGISTRY.yaml"
    state_path = ROOT / "01_governance/PROJECT_STATE.yaml"
    registry = require_mapping(load_yaml(registry_path), rel(registry_path))
    state = require_mapping(load_yaml(state_path), rel(state_path))

    tasks = registry.get("tasks")
    if not isinstance(tasks, list):
        raise ValidationError("TASK_REGISTRY.yaml must contain a top-level tasks list")

    task_by_id: dict[str, dict[str, Any]] = {}
    task_classes: dict[str, str] = {}
    for index, task_value in enumerate(tasks):
        task = require_mapping(task_value, f"tasks[{index}]")
        task_id = task.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            raise ValidationError(f"tasks[{index}] has no non-empty task_id")
        if task_id in task_by_id:
            raise ValidationError(f"Duplicate task_id: {task_id}")
        try:
            task_classes[task_id] = status_class(task.get("status"))
        except ValidationError as exc:
            raise ValidationError(f"Task {task_id}: {exc}") from exc
        task_by_id[task_id] = task

    dependencies: dict[str, list[str]] = {}
    for task_id, task in task_by_id.items():
        deps = require_string_list(task.get("dependencies", []), f"{task_id}.dependencies")
        unknown = sorted(set(deps) - set(task_by_id))
        if unknown:
            raise ValidationError(
                f"{task_id} has unknown dependencies: {', '.join(unknown)}"
            )
        if task_id in deps:
            raise ValidationError(f"{task_id} depends on itself")
        dependencies[task_id] = deps

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(task_id: str, stack: list[str]) -> None:
        if task_id in visited:
            return
        if task_id in visiting:
            cycle_start = stack.index(task_id)
            cycle = stack[cycle_start:] + [task_id]
            raise ValidationError(f"Task dependency cycle: {' -> '.join(cycle)}")
        visiting.add(task_id)
        stack.append(task_id)
        for dependency in dependencies[task_id]:
            visit(dependency, stack)
        stack.pop()
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in sorted(task_by_id):
        visit(task_id, [])

    # A verified label is usable only while its entire declared task dependency
    # closure remains completed. Traverse from each executable root so reopening
    # an upstream task invalidates every affected root, without requiring
    # unrelated tasks or treating decision_dependencies as task dependencies.
    # Missing references, self-dependencies and cycles are checked above.
    for task_id, deps in dependencies.items():
        if task_classes[task_id] in {"ready", "active"}:
            pending = list(deps)
            checked: set[str] = set()
            while pending:
                dependency = pending.pop()
                if dependency in checked:
                    continue
                if task_classes[dependency] != "completed":
                    raise ValidationError(
                        f"Task {task_id} has unsatisfied dependencies "
                        "(must be VERIFIED throughout dependency closure): "
                        f"{dependency} ({task_by_id[dependency]['status']})"
                    )
                checked.add(dependency)
                pending.extend(dependencies[dependency])

    listed: dict[str, str] = {}
    state_lists: dict[str, list[str]] = {}
    for field, expected_class in LIST_STATUS_CLASSES.items():
        ids = require_string_list(state.get(field, []), f"PROJECT_STATE.{field}")
        state_lists[field] = ids
        for task_id in ids:
            if task_id not in task_by_id:
                raise ValidationError(f"PROJECT_STATE.{field} contains unknown task {task_id}")
            if task_id in listed:
                raise ValidationError(
                    f"Task {task_id} appears in both {listed[task_id]} and {field}"
                )
            listed[task_id] = field
            actual_class = task_classes[task_id]
            if actual_class != expected_class:
                raise ValidationError(
                    f"Task {task_id} is listed in {field}, but registry status "
                    f"{task_by_id[task_id].get('status')!r} classifies as {actual_class}"
                )

    missing = sorted(set(task_by_id) - set(listed))
    if missing:
        raise ValidationError(
            f"PROJECT_STATE task lists are missing registry tasks: {', '.join(missing)}"
        )

    check_readme_routing(state, state_lists["ready_task_ids"])
    return len(task_by_id), sum(len(items) for items in state_lists.values())


def extract_mode(text: str) -> str | None:
    match = re.search(r"\bMODE:\s*[A-Z0-9_-]+", text)
    return match.group(0).replace("  ", " ") if match else None


def check_readme_routing(state: dict[str, Any], ready_ids: list[str]) -> None:
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    marker = "The next command for the planning model is:"
    if marker not in readme:
        raise ValidationError(f"README.md is missing the '{marker}' section")
    readme_mode = extract_mode(readme.split(marker, 1)[1])
    if readme_mode is None:
        raise ValidationError("README.md next-command section contains no MODE command")

    state_mode = extract_mode(str(state.get("next_recommended_action", "")))
    if state_mode is not None and readme_mode != state_mode:
        raise ValidationError(
            f"README next command {readme_mode!r} does not match "
            f"PROJECT_STATE next_recommended_action {state_mode!r}"
        )

    if len(ready_ids) == 1:
        expected = f"MODE: EXECUTE_TASK_{ready_ids[0]}"
        if readme_mode != expected:
            raise ValidationError(
                f"Exactly one task is READY ({ready_ids[0]}), but README routes to "
                f"{readme_mode!r} instead of {expected!r}"
            )


def check_secrets() -> tuple[int, int]:
    scanned = 0
    matches = 0
    for path in repo_files():
        lower_name = path.name.lower()
        if lower_name in FORBIDDEN_TRACKED_NAMES and lower_name != ".env.example":
            raise ValidationError(f"Forbidden credential-bearing filename is tracked: {rel(path)}")
        if path.suffix.lower() in FORBIDDEN_TRACKED_SUFFIXES:
            raise ValidationError(f"Forbidden secret-key file is tracked: {rel(path)}")
        try:
            with path.open("r", encoding="utf-8") as handle:
                line_number = 0
                while text := handle.readline(SECRET_SCAN_LINE_LIMIT + 1):
                    line_number += 1
                    if len(text) > SECRET_SCAN_LINE_LIMIT:
                        raise ValidationError(
                            f"Secret scan line length limit ({SECRET_SCAN_LINE_LIMIT} "
                            f"characters) exceeded in {rel(path)} line {line_number}; "
                            "cannot safely scan this file"
                        )
                    for label, pattern in SECRET_PATTERNS:
                        if pattern.search(text):
                            raise ValidationError(
                                f"Possible {label} in {rel(path)} line {line_number}; "
                                "replace it with a non-secret reference or synthetic marker"
                            )
        except UnicodeDecodeError:
            # Preserve non-UTF-8 binary detection without loading the full file.
            continue
        except OSError as exc:
            raise ValidationError(f"Secret scan could not read {rel(path)}: {exc}") from exc
        scanned += 1
    return scanned, matches


def check_frozen_digests() -> int:
    source_path = ROOT / FROZEN_DIGEST_SOURCE
    source = require_mapping(load_yaml(source_path), rel(source_path))
    pins = source.get("reviewed_artifact_digests_sha256")
    if not isinstance(pins, dict) or not pins:
        raise ValidationError(
            f"{FROZEN_DIGEST_SOURCE.as_posix()} has no reviewed_artifact_digests_sha256 map"
        )

    selected: dict[str, str] = {}
    for path_value, digest_value in pins.items():
        if not isinstance(path_value, str) or not isinstance(digest_value, str):
            raise ValidationError("Frozen digest map must contain string path/digest pairs")
        if (
            path_value.startswith("03_product/ENGINEERING_PREVIEW_")
            or path_value.startswith("05_architecture/")
            or path_value in FROZEN_EXACT_PATHS
        ):
            selected[path_value] = digest_value.lower()

    if not selected:
        raise ValidationError("Frozen digest selection is unexpectedly empty")

    for relative, expected in sorted(selected.items()):
        path = ROOT / relative
        if not path.is_file():
            raise ValidationError(f"Frozen artifact is missing: {relative}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise ValidationError(
                f"Frozen artifact digest mismatch for {relative}: "
                f"expected {expected}, got {actual}. A governed handback/checkpoint update is required."
            )
    return len(selected)


def main() -> int:
    checks: list[tuple[str, Any]] = []
    try:
        checks.append(("YAML files", check_yaml()))
        checks.append(("CSV files", check_csv()))
        checks.append(("JSON files", check_json()))
        task_count, listed_count = check_task_graph_and_state()
        checks.append(("Task registry entries", task_count))
        checks.append(("State-listed task entries", listed_count))
        scanned_files, secret_matches = check_secrets()
        checks.append(("Text files secret-scanned", scanned_files))
        checks.append(("Secret matches", secret_matches))
        checks.append(("Frozen digests verified", check_frozen_digests()))
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    for label, value in checks:
        print(f"PASS: {label}: {value}")
    print("PASS: repository governance validation complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
