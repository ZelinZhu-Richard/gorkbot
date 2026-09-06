"""Governance regressions using isolated temporary repository fixtures."""

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

from scripts import validate_governance as validator

REPOSITORY_ROOT = validator.ROOT


class GovernanceValidationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        root_patch = patch.object(validator, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        (self.root / "01_governance").mkdir()
        self.tasks = [
            {"task_id": "T-001", "status": "VERIFIED", "dependencies": []},
            {"task_id": "T-002", "status": "READY", "dependencies": ["T-001"]},
        ]
        self.state = {field: [] for field in validator.LIST_STATUS_CLASSES}
        self.state["completed_task_ids"] = ["T-001"]
        self.state["ready_task_ids"] = ["T-002"]
        (self.root / "README.md").write_text(
            "The next command for the planning model is:\n"
            "MODE: EXECUTE_TASK_T-002\n",
            encoding="utf-8",
        )

    def write_governance(self):
        for name, value in (
            ("TASK_REGISTRY", {"tasks": self.tasks}),
            ("PROJECT_STATE", self.state),
        ):
            (self.root / "01_governance" / f"{name}.yaml").write_text(
                yaml.safe_dump(value), encoding="utf-8"
            )

    def track(self, path):
        for args in (("init", "--quiet"), ("add", "--", path.name)):
            subprocess.run(
                ["git", "-C", str(self.root), *args],
                check=True, capture_output=True,
            )
        tracked = subprocess.check_output(
            ["git", "-C", str(self.root), "ls-files", "--", path.name], text=True
        )
        self.assertEqual(tracked.strip(), path.name)

    def test_valid_fixture_passes(self):
        self.write_governance()
        self.assertEqual(validator.check_task_graph_and_state(), (2, 2))

    def test_unknown_or_missing_status_fails_before_reconciliation(self):
        for status in ("VERIFED", None, "", "UNVERIFIED"):
            with self.subTest(status=status):
                self.tasks[0]["status"] = status
                self.write_governance()
                with self.assertRaisesRegex(
                    validator.ValidationError, "T-001.*[Uu]nrecognized task status"
                ):
                    validator.check_task_graph_and_state()
        del self.tasks[0]["status"]
        self.state["completed_task_ids"] = []
        self.write_governance()
        with self.assertRaisesRegex(
            validator.ValidationError, "T-001.*[Uu]nrecognized task status"
        ):
            validator.check_task_graph_and_state()

    def test_executable_tasks_require_verified_dependencies(self):
        for task_status in ("READY", "CLAIMED", "ACTIVE", "IN_PROGRESS"):
            for dependency_status in ("BACKLOG", "BLOCKED", "READY_FOR_REVIEW", "READY", "ACTIVE"):
                with self.subTest(task=task_status, dependency=dependency_status):
                    self.tasks[0]["status"] = dependency_status
                    self.tasks[1]["status"] = task_status
                    self.state = {field: [] for field in validator.LIST_STATUS_CLASSES}
                    for task in self.tasks:
                        task_class = validator.status_class(task["status"])
                        self.state[f"{task_class}_task_ids"].append(task["task_id"])
                    self.write_governance()
                    with self.assertRaisesRegex(
                        validator.ValidationError, "T-002.*unsatisfied dependencies.*T-001"
                    ):
                        validator.check_task_graph_and_state()

    def test_existing_status_vocabulary_is_preserved(self):
        expected = {
            "READY": "ready",
            "VERIFIED": "completed",
            "VERIFIED_PHASE_A_PROTOCOL_CRITERIA_NOT_EXECUTION_READY": "completed",
            "BACKLOG": "backlog",
            "BACKLOG_DO_NOT_RUN": "backlog",
            "BLOCKED": "blocked",
            "ACTIVE": "active",
            "CLAIMED": "active",
            "IN_PROGRESS": "active",
            "READY_FOR_REVIEW": "active",
        }
        for status, task_class in expected.items():
            with self.subTest(status=status):
                self.assertEqual(validator.status_class(status), task_class)
        self.tasks[0]["status"] = "VERIFIED_PHASE_A_PROTOCOL_CRITERIA_NOT_EXECUTION_READY"
        self.write_governance()
        self.assertEqual(validator.check_task_graph_and_state(), (2, 2))

    def write_dependency_chain(self, statuses):
        self.tasks = [
            {
                "task_id": f"T-{index:03d}",
                "status": status,
                "dependencies": [f"T-{index + 1:03d}"] if index < len(statuses) else [],
            }
            for index, status in enumerate(statuses, start=1)
        ]
        self.state = {field: [] for field in validator.LIST_STATUS_CLASSES}
        for task in self.tasks:
            task_class = validator.status_class(task["status"])
            self.state[f"{task_class}_task_ids"].append(task["task_id"])
        (self.root / "README.md").write_text(
            "The next command for the planning model is:\n"
            "MODE: EXECUTE_TASK_T-001\n", encoding="utf-8",
        )
        self.write_governance()

    def test_ready_verified_backlog_fails(self):
        self.write_dependency_chain(["READY", "VERIFIED", "BACKLOG"])
        with self.assertRaisesRegex(
            validator.ValidationError,
            r"Task T-001 has unsatisfied dependencies.*closure.*T-003 \(BACKLOG\)",
        ):
            validator.check_task_graph_and_state()

    def test_ready_verified_verified_backlog_fails(self):
        self.write_dependency_chain(["READY", "VERIFIED", "VERIFIED", "BACKLOG"])
        with self.assertRaisesRegex(
            validator.ValidationError,
            r"Task T-001 has unsatisfied dependencies.*closure.*T-004 \(BACKLOG\)",
        ):
            validator.check_task_graph_and_state()

    def test_ready_verified_verified_passes(self):
        self.write_dependency_chain(["READY", "VERIFIED", "VERIFIED"])
        self.assertEqual(validator.check_task_graph_and_state(), (3, 3))

    def test_transitive_incomplete_statuses_fail_for_executable_tasks(self):
        for root_status in ("READY", "CLAIMED", "ACTIVE", "IN_PROGRESS", "READY_FOR_REVIEW"):
            for leaf_status in ("BACKLOG", "BLOCKED", "READY", "READY_FOR_REVIEW", "ACTIVE"):
                with self.subTest(root=root_status, leaf=leaf_status):
                    self.write_dependency_chain([root_status, "VERIFIED", leaf_status])
                    with self.assertRaisesRegex(
                        validator.ValidationError,
                        rf"Task T-001 has unsatisfied dependencies.*closure.*T-003 \({leaf_status}\)",
                    ):
                        validator.check_task_graph_and_state()

    def test_transitive_unknown_and_unsupported_verified_statuses_fail(self):
        for status in ("UNKNOWN", "VERIFIED_ARBITRARY", "VERIFIED_PENDING_REVIEW", "VERIFIED_"):
            with self.subTest(status=status):
                self.write_dependency_chain(["READY", "VERIFIED", "VERIFIED"])
                self.tasks[2]["status"] = status
                self.write_governance()
                with self.assertRaisesRegex(
                    validator.ValidationError, "Task T-003: Unrecognized task status"
                ):
                    validator.check_task_graph_and_state()

    def test_supported_qualified_verified_status_requires_satisfied_closure(self):
        # PROJECT_STATE E3-002 uses this qualification for completed Phase A
        # protocol work; it grants no Phase B execution authority.
        qualified = "VERIFIED_PHASE_A_PROTOCOL_CRITERIA_NOT_EXECUTION_READY"
        self.write_dependency_chain(["READY", qualified, "VERIFIED"])
        self.assertEqual(validator.check_task_graph_and_state(), (3, 3))
        self.tasks[2]["status"] = "BACKLOG"
        self.state["completed_task_ids"].remove("T-003")
        self.state["backlog_task_ids"].append("T-003")
        self.write_governance()
        with self.assertRaisesRegex(
            validator.ValidationError, r"T-001.*unsatisfied dependencies.*closure.*T-003 \(BACKLOG\)"
        ):
            validator.check_task_graph_and_state()

    def test_reopening_verified_task_invalidates_each_downstream_ready_task(self):
        # Isolate each downstream root so fail-fast validation cannot hide one.
        for root in ("DIRECT", "TRANSITIVE", "DEEP"):
            with self.subTest(root=root):
                self.tasks = [
                    {"task_id": "UPSTREAM", "status": "VERIFIED", "dependencies": []},
                    {"task_id": "MID", "status": "VERIFIED", "dependencies": ["UPSTREAM"]},
                    {"task_id": "MID2", "status": "VERIFIED", "dependencies": ["MID"]},
                    *[
                        {"task_id": name, "status": "READY" if name == root else "BACKLOG",
                         "dependencies": [dependency]}
                        for name, dependency in (("DIRECT", "UPSTREAM"), ("TRANSITIVE", "MID"), ("DEEP", "MID2"))
                    ],
                ]
                self.state = {field: [] for field in validator.LIST_STATUS_CLASSES}
                self.state["completed_task_ids"] = ["UPSTREAM", "MID", "MID2"]
                self.state["ready_task_ids"] = [root]
                self.state["backlog_task_ids"] = [name for name in ("DIRECT", "TRANSITIVE", "DEEP") if name != root]
                (self.root / "README.md").write_text(
                    f"The next command for the planning model is:\nMODE: EXECUTE_TASK_{root}\n",
                    encoding="utf-8",
                )
                self.write_governance()
                self.assertEqual(validator.check_task_graph_and_state(), (6, 6))
                self.tasks[0]["status"] = "BACKLOG"
                self.state["completed_task_ids"].remove("UPSTREAM")
                self.state["backlog_task_ids"].append("UPSTREAM")
                self.write_governance()
                with self.assertRaisesRegex(
                    validator.ValidationError,
                    rf"Task {root} has unsatisfied dependencies.*UPSTREAM \(BACKLOG\)",
                ):
                    validator.check_task_graph_and_state()

    def test_dependency_structure_errors_still_fail(self):
        for dependencies, reason in (
            (["MISSING"], "T-003 has unknown dependencies: MISSING"),
            (["T-003"], "T-003 depends on itself"),
            (["T-002"], "Task dependency cycle: T-002 -> T-003 -> T-002"),
        ):
            with self.subTest(reason=reason):
                self.write_dependency_chain(["READY", "VERIFIED", "VERIFIED"])
                self.tasks[2]["dependencies"] = dependencies
                self.write_governance()
                with self.assertRaisesRegex(validator.ValidationError, reason):
                    validator.check_task_graph_and_state()

    def test_unrelated_tasks_and_non_task_dependencies_are_not_required(self):
        self.write_dependency_chain(["READY", "VERIFIED", "VERIFIED"])
        self.tasks[1]["decision_dependencies"] = ["D-MISSING"]
        self.tasks[1]["blocked_by"] = ["UNRELATED"]
        self.tasks.extend([
            {"task_id": "UNRELATED", "status": "BACKLOG", "dependencies": []},
            {"task_id": "HISTORICAL", "status": "VERIFIED", "dependencies": ["UNRELATED"]},
        ])
        self.state["backlog_task_ids"].append("UNRELATED")
        self.state["completed_task_ids"].append("HISTORICAL")
        self.write_governance()
        self.assertEqual(validator.check_task_graph_and_state(), (5, 5))

    def test_real_repository_dependency_graph_passes(self):
        for relative in ("01_governance/TASK_REGISTRY.yaml", "01_governance/PROJECT_STATE.yaml", "README.md"):
            shutil.copyfile(REPOSITORY_ROOT / relative, self.root / relative)
        task_count = len(yaml.safe_load((self.root / "01_governance/TASK_REGISTRY.yaml").read_text())["tasks"])
        self.assertEqual(validator.check_task_graph_and_state(), (task_count, task_count))

    def test_omitted_only_ready_task_fails(self):
        self.state["ready_task_ids"] = []
        self.write_governance()
        with self.assertRaisesRegex(
            validator.ValidationError, "PROJECT_STATE.*missing.*T-002"
        ):
            validator.check_task_graph_and_state()

    def test_state_list_unknown_and_duplicate_ids_fail(self):
        for field, task_id, message in (
            ("ready_task_ids", "T-999", "unknown task T-999"),
            ("ready_task_ids", "T-002", "duplicate task IDs"),
            ("backlog_task_ids", "T-002", "appears in both"),
        ):
            with self.subTest(field=field, task_id=task_id):
                self.state[field].append(task_id)
                self.write_governance()
                with self.assertRaisesRegex(validator.ValidationError, message):
                    validator.check_task_graph_and_state()
                self.state[field].pop()

    def test_large_tracked_text_secret_fails(self):
        path = self.root / "large.txt"
        # Construct a deliberately fake pattern; never store a credential literal.
        fake_token = "gh" + "p_" + "A" * 36
        with path.open("w", encoding="utf-8") as handle:
            for _ in range(6000):
                handle.write("x" * 1000 + "\n")
            handle.write(fake_token + "\n")
        self.assertGreater(path.stat().st_size, 5_000_000)
        self.track(path)
        with self.assertRaisesRegex(
            validator.ValidationError, "Possible GitHub token in large.txt line 6001"
        ) as error:
            validator.check_secrets()
        self.assertNotIn(fake_token, str(error.exception))

    def test_large_tracked_clean_text_passes(self):
        path = self.root / "large.txt"
        with path.open("w", encoding="utf-8") as handle:
            for _ in range(6000):
                handle.write("x" * 1000 + "\n")
        self.track(path)
        self.assertEqual(validator.check_secrets(), (2, 0))

    def test_oversized_line_fails_closed(self):
        path = self.root / "long-line.txt"
        with path.open("w", encoding="utf-8") as handle:
            for _ in range(6000):
                handle.write("x" * 1000)
        self.track(path)
        with self.assertRaisesRegex(
            validator.ValidationError, "Secret scan.*line.*limit.*long-line.txt"
        ):
            validator.check_secrets()

    def test_large_binary_is_not_loaded_as_text(self):
        path = self.root / "binary.dat"
        with path.open("wb") as handle:
            handle.write(b"\xff\xfe")
            handle.truncate(6_000_000)
        self.track(path)
        self.assertEqual(validator.check_secrets(), (1, 0))


if __name__ == "__main__":
    unittest.main()
