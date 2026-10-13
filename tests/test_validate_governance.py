"""Governance regressions using isolated temporary repository fixtures."""

import io
import os
import shutil
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr
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
        self.set_current_command("MODE: EXECUTE_TASK_T-002")

    def set_current_command(self, command):
        self.state["next_recommended_action"] = command
        (self.root / "README.md").write_text(
            "The next command for the planning model is:\n\n"
            f"```text\n{command}\n```\n", encoding="utf-8",
        )

    def write_governance(self):
        for name, value in (
            ("TASK_REGISTRY", {"tasks": self.tasks}),
            ("PROJECT_STATE", self.state),
        ):
            (self.root / "01_governance" / f"{name}.yaml").write_text(
                yaml.safe_dump(value), encoding="utf-8"
            )

    def track(self, path, force=False):
        relative = path.relative_to(self.root).as_posix()
        add_args = ("add", *(["-f"] if force else []), "--", relative)
        for args in (("init", "--quiet"), add_args):
            subprocess.run(
                ["git", "--literal-pathspecs", *args],
                cwd=self.root, check=True, capture_output=True,
            )
        tracked = subprocess.check_output(
            ["git", "--literal-pathspecs", "ls-files", "--cached", "-z", "--", relative],
            cwd=self.root,
        )
        self.assertEqual(tracked, os.fsencode(relative) + b"\0")

    def write_routing_fixture(self, statuses, command):
        # All execution candidates have a completed prerequisite, isolating
        # route failures from dependency and state-list failures.
        self.tasks = [
            {"task_id": "PREREQUISITE", "status": "VERIFIED", "dependencies": []},
            *[
                {"task_id": task_id, "status": status, "dependencies": ["PREREQUISITE"]}
                for task_id, status in statuses.items()
            ],
        ]
        self.state = {field: [] for field in validator.LIST_STATUS_CLASSES}
        for task in self.tasks:
            task_class = validator.status_class(task["status"])
            self.state[f"{task_class}_task_ids"].append(task["task_id"])
        self.set_current_command(command)
        self.write_governance()

    def test_backlog_execution_fails_with_zero_one_or_multiple_ready_tasks(self):
        for ready_count in (0, 1, 2):
            with self.subTest(ready_count=ready_count):
                statuses = {"TARGET": "BACKLOG"}
                statuses.update({f"READY-{i}": "READY" for i in range(ready_count)})
                self.write_routing_fixture(statuses, "MODE: EXECUTE_TASK_TARGET")
                with self.assertRaisesRegex(
                    validator.ValidationError, "EXECUTE_TASK target 'TARGET'.*ineligible status 'BACKLOG'"
                ):
                    validator.check_task_graph_and_state()

    def test_claimed_execution_passes_with_zero_one_or_multiple_ready_tasks(self):
        for ready_count in (0, 1, 2):
            with self.subTest(ready_count=ready_count):
                statuses = {"TARGET": "CLAIMED"}
                statuses.update({f"READY-{i}": "READY" for i in range(ready_count)})
                self.write_routing_fixture(statuses, "MODE: EXECUTE_TASK_TARGET")
                self.assertEqual(validator.check_task_graph_and_state(), (2 + ready_count,) * 2)

    def test_multiple_ready_tasks_can_route_to_either(self):
        for target in ("FIRST", "SECOND"):
            with self.subTest(target=target):
                self.write_routing_fixture(
                    {"FIRST": "READY", "SECOND": "READY"}, f"MODE: EXECUTE_TASK_{target}"
                )
                self.assertEqual(validator.check_task_graph_and_state(), (3, 3))

    def test_nonexecutable_statuses_cannot_receive_execution_routes(self):
        for status in (
            "READY_FOR_REVIEW", "VERIFIED", "BLOCKED", "ACTIVE", "IN_PROGRESS",
            "CLAIMED_PENDING_APPROVAL", "READY_FOR_REVIEW_FIXES",
            "VERIFIED_PHASE_A_PROTOCOL_CRITERIA_NOT_EXECUTION_READY",
        ):
            with self.subTest(status=status):
                self.write_routing_fixture({"TARGET": status}, "MODE: EXECUTE_TASK_TARGET")
                with self.assertRaisesRegex(
                    validator.ValidationError,
                    f"EXECUTE_TASK target 'TARGET'.*ineligible status '{status}'.*READY or CLAIMED",
                ):
                    validator.check_task_graph_and_state()

    def test_unknown_execution_target_fails(self):
        self.write_routing_fixture({}, "MODE: EXECUTE_TASK_MISSING")
        with self.assertRaisesRegex(
            validator.ValidationError, "EXECUTE_TASK target 'MISSING' is not in TASK_REGISTRY"
        ):
            validator.check_task_graph_and_state()

    def test_review_reproduction_matching_execution_typo_is_rejected(self):
        # Copy the real, valid graph; E3-003 is READY with satisfied dependencies.
        for relative in ("01_governance/TASK_REGISTRY.yaml", "01_governance/PROJECT_STATE.yaml"):
            shutil.copyfile(REPOSITORY_ROOT / relative, self.root / relative)
        self.tasks = yaml.safe_load((self.root / "01_governance/TASK_REGISTRY.yaml").read_text())["tasks"]
        self.state = yaml.safe_load((self.root / "01_governance/PROJECT_STATE.yaml").read_text())
        self.set_current_command("MODE: EXECUTE-TASK_E3-003")
        self.write_governance()
        with self.assertRaisesRegex(
            validator.ValidationError, "Unrecognized MODE command: 'EXECUTE-TASK_E3-003'"
        ):
            validator.check_task_graph_and_state()

    def test_execution_like_unknown_modes_fail_regardless_of_ready_count(self):
        for ready_count in (0, 1, 2):
            for prefix in ("EXECUTE-TASK", "EXECUTE_TASKS", "RUN_TASK", "EXECUTE"):
                for target in ("E3-003", "MISSING"):
                    mode = f"{prefix}_{target}"
                    with self.subTest(ready_count=ready_count, mode=mode):
                        statuses = {"E3-003": "BACKLOG"}
                        statuses.update({f"READY-{i}": "READY" for i in range(ready_count)})
                        self.write_routing_fixture(statuses, f"MODE: {mode}")
                        with self.assertRaisesRegex(
                            validator.ValidationError, f"Unrecognized MODE command: '{mode}'"
                        ):
                            validator.check_task_graph_and_state()

    def test_unknown_modes_fail_even_with_ready_apparent_targets(self):
        for mode in (
            "EXECUTE-TASK_E3-003", "EXECUTE_TASKS_E3-003", "RUN_TASK_E3-003",
            "EXECUTE_E3-003", "VERIFY-TASK_E3-002", "STATUS_EXTRA", "SOMETHING_UNKNOWN",
            "REVIEW_ANYTHING", "VERIFY_ANYTHING", "PLAN_ANYTHING", "AUDIT_ANYTHING",
            "RUN_ANYTHING", "EXECUTE_ANYTHING", "INITIALIZE_ENGINEERING_PREVIEW_EXTRA",
        ):
            with self.subTest(mode=mode):
                self.write_routing_fixture(
                    {"E3-003": "READY", "E3-002": "READY"}, f"MODE: {mode}"
                )
                with self.assertRaisesRegex(
                    validator.ValidationError, f"Unrecognized MODE command: '{mode}'"
                ):
                    validator.check_task_graph_and_state()

    def test_parameterized_families_require_nonempty_well_formed_suffixes(self):
        for family in (
            "EXECUTE_TASK", "REVIEW_TASK", "FIX_TASK", "VERIFY_TASK", "PLAN_STAGE", "VERIFY_STAGE",
        ):
            for suffix, reason in (
                ("", "Unrecognized MODE command"),
                ("_", "malformed MODE command"),
                ("__E3-003", "malformed MODE command"),
                ("_E3-003_", "malformed MODE command"),
                ("_E3--003", "malformed MODE command"),
                ("_E3-003/OTHER", "malformed MODE command"),
                ("_E3-003.extra", "malformed MODE command"),
                ("_e3-003", "malformed MODE command"),
            ):
                with self.subTest(family=family, suffix=suffix):
                    # Even a matching registry entry cannot permit malformed syntax.
                    statuses = {suffix[1:]: "READY"} if suffix[1:] else {}
                    self.write_routing_fixture(statuses, f"MODE: {family}{suffix}")
                    with self.assertRaisesRegex(validator.ValidationError, reason):
                        validator.check_task_graph_and_state()

    def test_stage_families_reject_nonnumeric_and_partial_suffixes(self):
        for family in ("PLAN_STAGE", "VERIFY_STAGE"):
            for stage in ("E", "S3", "THREE", "3E", "E3_EXTRA", "3_EXTRA", "E3-003"):
                with self.subTest(family=family, stage=stage):
                    self.write_routing_fixture({}, f"MODE: {family}_{stage}")
                    with self.assertRaisesRegex(validator.ValidationError, "Unrecognized MODE command"):
                        validator.check_task_graph_and_state()

    def test_all_documented_literal_modes_and_authorized_extension_pass(self):
        # Independent expectations from MASTER_OPERATING_PROMPT, Operating modes,
        # plus TASK_REGISTRY E0-001-A1; do not import the implementation's allowlist.
        for mode in (
            "INITIALIZE", "STATUS", "ADVANCE_STAGE", "AUDIT_ARCHITECTURE", "AUDIT_SECURITY",
            "AUDIT_PRODUCT", "BENCHMARK_MODELS", "PREPARE_VC", "RESUME",
            "INITIALIZE_ENGINEERING_PREVIEW",
        ):
            with self.subTest(mode=mode):
                self.write_routing_fixture({"E3-003": "BACKLOG"}, f"MODE: {mode}")
                self.assertEqual(validator.check_task_graph_and_state(), (2, 2))

    def test_documented_parameterized_families_and_suffix_conventions_pass(self):
        for family in ("EXECUTE_TASK", "REVIEW_TASK", "FIX_TASK", "VERIFY_TASK"):
            for target in ("S0-001", "S12-001", "E0-001", "E3-003", "E5-001", "TARGET", "TASK_1-A"):
                with self.subTest(family=family, target=target):
                    status = "READY" if family == "EXECUTE_TASK" else "BACKLOG"
                    self.write_routing_fixture({target: status}, f"MODE: {family}_{target}")
                    self.assertEqual(validator.check_task_graph_and_state(), (2, 2))
        for family in ("PLAN_STAGE", "VERIFY_STAGE"):
            for stage in ("0", "1", "12", "E0", "E3", "E5"):
                with self.subTest(family=family, stage=stage):
                    self.write_routing_fixture({}, f"MODE: {family}_{stage}")
                    self.assertEqual(validator.check_task_graph_and_state(), (1, 1))

    def test_nonexecution_task_targets_require_registry_membership(self):
        for family in ("REVIEW_TASK", "FIX_TASK", "VERIFY_TASK"):
            with self.subTest(family=family):
                self.write_routing_fixture({}, f"MODE: {family}_MISSING")
                with self.assertRaisesRegex(
                    validator.ValidationError, f"{family} target 'MISSING' is not in TASK_REGISTRY"
                ):
                    validator.check_task_graph_and_state()

    def test_nonexecution_task_modes_do_not_require_execution_eligible_status(self):
        for family in ("REVIEW_TASK", "FIX_TASK", "VERIFY_TASK"):
            for status in ("BACKLOG", "BLOCKED", "VERIFIED", "READY_FOR_REVIEW", "IN_PROGRESS"):
                with self.subTest(family=family, status=status):
                    self.write_routing_fixture({"E3-002": status}, f"MODE: {family}_E3-002")
                    self.assertEqual(validator.check_task_graph_and_state(), (2, 2))

    def test_readme_state_command_mismatch_fails(self):
        self.write_routing_fixture({"TARGET": "READY"}, "MODE: EXECUTE_TASK_TARGET")
        self.state["next_recommended_action"] = "MODE: REVIEW_TASK_TARGET"
        self.write_governance()
        with self.assertRaisesRegex(validator.ValidationError, "README next command.*does not match"):
            validator.check_task_graph_and_state()

    def test_missing_state_command_cannot_disable_route_checks(self):
        for value in (None, "", 17, "Follow the README"):
            with self.subTest(value=value):
                self.state["next_recommended_action"] = value
                self.write_governance()
                with self.assertRaisesRegex(
                    validator.ValidationError, "PROJECT_STATE.next_recommended_action.*exactly one MODE"
                ):
                    validator.check_task_graph_and_state()
        del self.state["next_recommended_action"]
        self.write_governance()
        with self.assertRaisesRegex(
            validator.ValidationError, "PROJECT_STATE.next_recommended_action.*exactly one MODE"
        ):
            validator.check_task_graph_and_state()

    def test_malformed_and_ambiguous_commands_fail_in_each_source(self):
        for command, reason in (
            ("MODE: EXECUTE_TASK", "Unrecognized MODE command: 'EXECUTE_TASK'"),
            ("MODE: EXECUTE_TASK_", "malformed MODE command"),
            ("MODE: EXECUTE_TASK_T-002/OTHER", "malformed MODE command"),
            ("MODE: EXECUTE_TASK_T-002 or T-001", "malformed MODE command"),
            ("MODE: EXECUTE_TASK_T-002.extra", "malformed MODE command"),
            ("MODE: EXECUTE_TASK_T-002; MODE: EXECUTE_TASK_T-001", "exactly one MODE"),
            ("MODE: EXECUTE_TASK_T-002\nMODE: EXECUTE_TASK_T-001", "exactly one MODE"),
            ("No current command", "exactly one MODE"),
        ):
            # Incomplete families reach mode recognition only if both sources
            # agree; parser errors are also exercised in each source.
            for source in ("both", "readme", "state") if command != "MODE: EXECUTE_TASK" else ("both",):
                with self.subTest(command=command, source=source):
                    self.set_current_command(command if source != "state" else "MODE: EXECUTE_TASK_T-002")
                    if source == "readme":
                        self.state["next_recommended_action"] = "MODE: EXECUTE_TASK_T-002"
                    elif source == "state":
                        self.state["next_recommended_action"] = command
                    self.write_governance()
                    with self.assertRaisesRegex(validator.ValidationError, reason):
                        validator.check_task_graph_and_state()

    def test_nonexecution_modes_preserved_with_zero_or_one_ready_task(self):
        for ready_count in (0, 1):
            for mode in (
                "REVIEW_TASK_TARGET", "VERIFY_TASK_TARGET", "FIX_TASK_TARGET",
                "PLAN_STAGE_E3", "VERIFY_STAGE_E3", "ADVANCE_STAGE", "STATUS", "RESUME",
            ):
                with self.subTest(ready_count=ready_count, mode=mode):
                    statuses = {"TARGET": "READY_FOR_REVIEW"}
                    if ready_count:
                        statuses["OTHER"] = "READY"
                    self.write_routing_fixture(statuses, f"MODE: {mode}")
                    self.assertEqual(validator.check_task_graph_and_state(), (2 + ready_count,) * 2)

    def test_only_designated_readme_block_is_routed(self):
        readme = self.root / "README.md"
        readme.write_text(
            "## Historical example\n```text\nMODE: EXECUTE_TASK_MISSING\n```\n\n"
            + readme.read_text(encoding="utf-8")
            + "\n## Other examples\n```text\nMODE: EXECUTE_TASK_T-001\n```\n"
            + "\n## Historical typo\n```text\nMODE: EXECUTE-TASK_E3-003\n```\n",
            encoding="utf-8",
        )
        self.state["next_recommended_action"] += " — execute only this registry entry."
        self.write_governance()
        self.assertEqual(validator.check_task_graph_and_state(), (2, 2))

    def test_missing_or_ambiguous_readme_block_cannot_use_later_examples(self):
        marker = "The next command for the planning model is:"
        for text, reason in (
            ("## History\nMODE: EXECUTE_TASK_T-002\n", "exactly one current-command marker"),
            (f"{marker}\n\n## History\n```text\nMODE: EXECUTE_TASK_T-002\n```\n", "missing or malformed"),
            (f"{marker}\n\n```text\nNo command\n```\n\nMODE: EXECUTE_TASK_T-002\n", "exactly one MODE"),
            (f"{marker}\n```text\nMODE: EXECUTE_TASK_T-002\n", "missing or malformed"),
            (f"{marker}\n```text\nMODE: EXECUTE_TASK_T-002\n```\n{marker}\n", "exactly one current-command marker"),
        ):
            with self.subTest(reason=reason):
                (self.root / "README.md").write_text(text, encoding="utf-8")
                self.write_governance()
                with self.assertRaisesRegex(validator.ValidationError, reason):
                    validator.check_task_graph_and_state()

    def test_commented_readme_command_is_not_the_current_command(self):
        readme = self.root / "README.md"
        block = readme.read_text(encoding="utf-8")
        self.write_governance()
        for comment_end in ("-->\n", ""):
            with self.subTest(closed_comment=bool(comment_end)):
                readme.write_text("<!--\n" + block + comment_end, encoding="utf-8")
                with self.assertRaisesRegex(validator.ValidationError, "exactly one current-command marker"):
                    validator.check_task_graph_and_state()
        readme.write_text("<!--\n" + block + "-->\n" + block, encoding="utf-8")
        self.assertEqual(validator.check_task_graph_and_state(), (2, 2))

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
        self.set_current_command("MODE: EXECUTE_TASK_T-001")
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
                self.set_current_command(f"MODE: EXECUTE_TASK_{root}")
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

    def test_large_binary_is_explicitly_rejected(self):
        path = self.root / "binary.dat"
        with path.open("wb") as handle:
            handle.write(b"\xff\xfe")
            handle.truncate(6_000_000)
        self.track(path)
        with self.assertRaisesRegex(
            validator.ValidationError, "requires UTF-8 text; undecodable file: 'binary.dat'"
        ):
            validator.check_secrets()

    def test_forced_tracked_secrets_in_excluded_directories_fail(self):
        ignored = ("build", "dist", "coverage", "node_modules")
        (self.root / ".gitignore").write_text(
            "".join(f"{directory}/\n" for directory in ignored), encoding="utf-8"
        )
        fake_token = "gh" + "p_" + "A" * 36
        for prefix in (Path(), Path("nested parent")):
            for directory in ignored:
                relative = prefix / directory / "fixture with spaces.txt"
                with self.subTest(path=relative):
                    path = self.root / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(fake_token + "\n", encoding="utf-8")
                    self.track(path, force=True)
                    with self.assertRaises(validator.ValidationError) as error:
                        validator.check_secrets()
                    self.assertIn(f"Possible GitHub token in {relative.as_posix()} line 1", str(error.exception))
                    self.assertNotIn(fake_token, str(error.exception))
                    # Keep earlier indexed fixtures clean so each negative
                    # fails for its own path, even in a fail-fast scanner.
                    path.write_text("clean UTF-8 fixture\n", encoding="utf-8")

    def test_clean_forced_tracked_file_is_included_and_passes(self):
        (self.root / ".gitignore").write_text("build/\n", encoding="utf-8")
        path = self.root / "nested parent/build/clean file.txt"
        path.parent.mkdir(parents=True)
        path.write_text("clean text\n", encoding="utf-8")
        self.track(path, force=True)
        paths = validator.security_files()
        self.assertIn(path, paths)
        self.assertEqual(validator.check_secrets(), (len(paths), 0))

    def test_ignored_untracked_generated_file_is_excluded(self):
        (self.root / ".gitignore").write_text("build/\n", encoding="utf-8")
        self.track(self.root / "README.md")
        path = self.root / "build/generated.txt"
        path.parent.mkdir()
        path.write_text("gh" + "p_" + "A" * 36, encoding="utf-8")
        self.assertNotIn(path, validator.security_files())
        self.assertEqual(validator.check_secrets(), (2, 0))

    def test_nonignored_untracked_file_is_scanned(self):
        self.track(self.root / "README.md")
        path = self.root / "untracked.txt"
        path.write_text("gh" + "p_" + "A" * 36, encoding="utf-8")
        with self.assertRaisesRegex(validator.ValidationError, "Possible GitHub token in untracked.txt"):
            validator.check_secrets()

    def test_index_paths_use_working_tree_bytes(self):
        path = self.root / "changed.txt"
        path.write_text("clean indexed content\n", encoding="utf-8")
        self.track(path)
        path.write_text("gh" + "p_" + "A" * 36, encoding="utf-8")
        with self.assertRaisesRegex(validator.ValidationError, "Possible GitHub token in changed.txt"):
            validator.check_secrets()

    def test_nul_delimited_paths_preserve_newlines_tabs_and_spaces(self):
        path = self.root / "nested directory/line\nbreak\tname [1].txt"
        path.parent.mkdir()
        path.write_text("clean text\n", encoding="utf-8")
        self.track(path)
        self.assertIn(path, validator.security_files())
        self.assertEqual(validator.check_secrets(), (2, 0))
        path.write_text("gh" + "p_" + "A" * 36, encoding="utf-8")
        with self.assertRaises(validator.ValidationError) as error:
            validator.check_secrets()
        self.assertIn(path.relative_to(self.root).as_posix(), str(error.exception))
        self.assertIn("Possible GitHub token", str(error.exception))

    def test_security_file_enumeration_deduplicates_paths(self):
        path = self.root / "duplicate.txt"
        path.write_text("clean text\n", encoding="utf-8")
        self.track(path)
        real_run = subprocess.run

        def duplicate_records(*args, **kwargs):
            result = real_run(*args, **kwargs)
            result.stdout += result.stdout
            return result

        with patch.object(validator.subprocess, "run", side_effect=duplicate_records):
            self.assertEqual(validator.check_secrets(), (2, 0))

    def test_git_enumeration_failure_fails_closed(self):
        # A real nonrepository directory must fail rather than use rglob.
        with self.assertRaisesRegex(validator.ValidationError, "Git file enumeration failed"):
            validator.check_secrets()
        self.track(self.root / "README.md")
        real_run = subprocess.run
        for failing_option in ("--cached", "--others"):
            with self.subTest(option=failing_option):
                def fail_enumeration(args, **kwargs):
                    if failing_option in args:
                        raise subprocess.CalledProcessError(1, args, stderr=b"untrusted stderr sentinel")
                    return real_run(args, **kwargs)

                with patch.object(validator.subprocess, "run", side_effect=fail_enumeration):
                    with self.assertRaisesRegex(validator.ValidationError, "Git file enumeration failed") as error:
                        validator.check_secrets()
                self.assertNotIn("untrusted stderr sentinel", str(error.exception))
        with patch.object(validator.subprocess, "run", side_effect=FileNotFoundError):
            with self.assertRaisesRegex(validator.ValidationError, "Git file enumeration failed"):
                validator.check_secrets()

    def test_malformed_git_enumeration_fails_closed(self):
        self.track(self.root / "README.md")
        for output, reason in (
            (b"unterminated", "not NUL-delimited"),
            (b"\0", "empty entry"),
            (b"invalid\0", "index enumeration is malformed"),
            (b"100644 abc 0\t../outside.txt\0", "unsafe path"),
        ):
            with self.subTest(reason=reason):
                result = subprocess.CompletedProcess([], 0, stdout=output)
                with patch.object(validator.subprocess, "run", return_value=result):
                    with self.assertRaisesRegex(validator.ValidationError, reason):
                        validator.check_secrets()

    def test_git_repository_overrides_cannot_hide_tracked_files(self):
        (self.root / ".gitignore").write_text("build/\n", encoding="utf-8")
        path = self.root / "build/forced.txt"
        path.parent.mkdir()
        path.write_text("gh" + "p_" + "A" * 36, encoding="utf-8")
        self.track(path, force=True)
        for variable in ("GIT_INDEX_FILE", "GIT_DIR", "GIT_COMMON_DIR", "GIT_WORK_TREE"):
            with self.subTest(variable=variable):
                with patch.dict(os.environ, {variable: str(self.root / "alternate-nonexistent")}):
                    with self.assertRaisesRegex(
                        validator.ValidationError, f"does not support Git repository/index overrides: {variable}"
                    ):
                        validator.check_secrets()

    def test_main_scans_credentials_before_format_errors(self):
        fake_token = "gh" + "p_" + "A" * 36
        path = self.root / "invalid.yaml"
        path.write_text("alias: *" + fake_token + "\n", encoding="utf-8")
        self.track(path)
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            self.assertEqual(validator.main(), 1)
        self.assertTrue(
            "Possible GitHub token in invalid.yaml line 1" in stderr.getvalue(),
            "Expected safe secret-scan diagnostic before YAML parsing",
        )
        self.assertFalse(fake_token in stderr.getvalue(), "Diagnostic leaked the synthetic marker")
        self.assertFalse("alias:" in stderr.getvalue(), "Diagnostic leaked file contents")

    def test_main_rejects_tracked_symlink_before_parsing_external_content(self):
        fake_token = "gh" + "p_" + "A" * 36
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / "external.yaml"
            external.write_text("alias: *" + fake_token + "\n", encoding="utf-8")
            path = self.root / "external.yaml"
            path.symlink_to(external)
            self.track(path)
            stderr = io.StringIO()
            with redirect_stderr(stderr):
                self.assertEqual(validator.main(), 1)
        self.assertTrue(
            "unsupported indexed entry 'external.yaml'" in stderr.getvalue(),
            "Expected indexed symlink rejection before YAML parsing",
        )
        self.assertFalse(fake_token in stderr.getvalue(), "Diagnostic leaked the synthetic marker")
        self.assertFalse(str(external) in stderr.getvalue(), "Diagnostic exposed an outside path")

    def test_missing_tracked_file_fails_closed(self):
        path = self.root / "missing.txt"
        path.write_text("clean text\n", encoding="utf-8")
        self.track(path)
        path.unlink()
        with self.assertRaisesRegex(validator.ValidationError, "could not read 'missing.txt'.*FileNotFoundError"):
            validator.check_secrets()

    def test_tracked_symlink_is_explicitly_rejected(self):
        path = self.root / "link.txt"
        path.symlink_to("README.md")
        self.track(path)
        with self.assertRaisesRegex(validator.ValidationError, "unsupported indexed entry 'link.txt'"):
            validator.check_secrets()
        # An indexed symlink stays unsupported even if the worktree contains
        # a regular file at that path.
        path.unlink()
        path.write_text("clean text\n", encoding="utf-8")
        with self.assertRaisesRegex(validator.ValidationError, "unsupported indexed entry 'link.txt'"):
            validator.check_secrets()

    def test_symlinked_worktree_leaf_or_ancestor_is_not_followed(self):
        with tempfile.TemporaryDirectory() as outside:
            outside_path = Path(outside) / "file.txt"
            outside_path.write_text("gh" + "p_" + "A" * 36, encoding="utf-8")
            directory = self.root / "parent"
            directory.mkdir()
            path = directory / "file.txt"
            path.write_text("clean text\n", encoding="utf-8")
            self.track(path)
            path.unlink()
            path.symlink_to(outside_path)
            with self.assertRaisesRegex(validator.ValidationError, "could not read 'parent/file.txt'.*symlinks are not followed"):
                validator.check_secrets()
            path.unlink()
            directory.rmdir()
            directory.symlink_to(outside, target_is_directory=True)
            # Ignore the new untracked symlink itself so the scanner must
            # exercise the mandatory indexed child through its ancestor.
            (self.root / ".gitignore").write_text("/parent\n", encoding="utf-8")
            with self.assertRaisesRegex(validator.ValidationError, "could not read 'parent/file.txt'.*symlinks are not followed"):
                validator.check_secrets()

    def test_nonregular_worktree_entry_fails_without_blocking(self):
        path = self.root / "nonregular.txt"
        path.write_text("clean text\n", encoding="utf-8")
        self.track(path)
        path.unlink()
        path.mkdir()
        with self.assertRaisesRegex(validator.ValidationError, "unsupported nonregular file: 'nonregular.txt'"):
            validator.check_secrets()
        path.rmdir()
        os.mkfifo(path)
        with self.assertRaisesRegex(validator.ValidationError, "unsupported nonregular file: 'nonregular.txt'"):
            validator.check_secrets()

    def test_index_gitlink_is_explicitly_rejected(self):
        self.track(self.root / "README.md")
        # Construct a local commit object without creating any branch commit.
        tree = subprocess.check_output(["git", "write-tree"], cwd=self.root).strip()
        commit = b"tree " + tree + b"\nauthor Test <test@example.invalid> 0 +0000\ncommitter Test <test@example.invalid> 0 +0000\n\nfixture\n"
        oid = subprocess.check_output(
            ["git", "hash-object", "-t", "commit", "-w", "--stdin"], input=commit, cwd=self.root,
        ).strip().decode("ascii")
        subprocess.run(
            ["git", "update-index", "--add", "--cacheinfo", f"160000,{oid},submodule"],
            cwd=self.root, check=True, capture_output=True,
        )
        (self.root / "submodule").mkdir()
        with self.assertRaisesRegex(validator.ValidationError, "unsupported indexed entry 'submodule'"):
            validator.check_secrets()

    def test_invalid_utf8_before_later_credential_fails(self):
        path = self.root / "invalid-first.txt"
        fake_token = "gh" + "p_" + "A" * 36
        path.write_bytes(b"\xff\n" + b"clean line\n" * 2000 + fake_token.encode() + b"\n")
        self.track(path)
        with self.assertRaisesRegex(validator.ValidationError, "requires UTF-8 text; undecodable file: 'invalid-first.txt'") as error:
            validator.check_secrets()
        self.assertNotIn(fake_token, str(error.exception))

    def test_credential_before_later_decoding_error_fails(self):
        path = self.root / "credential-first.txt"
        fake_token = "gh" + "p_" + "A" * 36
        for spacing, reason in (
            (b"", "requires UTF-8 text; undecodable file"),
            (b"clean line\n" * 2000, "Possible GitHub token"),
        ):
            with self.subTest(buffered_together=not spacing):
                path.write_bytes(fake_token.encode() + b"\n" + spacing + b"\xff")
                self.track(path)
                with self.assertRaisesRegex(validator.ValidationError, reason) as error:
                    validator.check_secrets()
                self.assertIn("credential-first.txt", str(error.exception))
                self.assertNotIn(fake_token, str(error.exception))

    def test_mixed_encoding_with_credential_beyond_five_mb_fails(self):
        path = self.root / "mixed.txt"
        fake_token = "gh" + "p_" + "A" * 36
        with path.open("wb") as handle:
            for _ in range(6000):
                handle.write(b"x" * 1000 + b"\n")
            self.assertGreater(handle.tell(), 5_000_000)
            handle.write(b"\xff\n" + fake_token.encode() + b"\n")
        self.track(path)
        with self.assertRaisesRegex(validator.ValidationError, "requires UTF-8 text; undecodable file: 'mixed.txt'") as error:
            validator.check_secrets()
        self.assertNotIn(fake_token, str(error.exception))

    def test_utf16_credentials_fail_with_or_without_bom(self):
        path = self.root / "utf16.txt"
        fake_token = "gh" + "p_" + "A" * 36
        for encoding, bom in (("utf-16-le", b"\xff\xfe"), ("utf-16-be", b"\xfe\xff")):
            for prefix in (bom, b""):
                with self.subTest(encoding=encoding, bom=bool(prefix)):
                    path.write_bytes(prefix + (fake_token + "\n").encode(encoding))
                    self.track(path)
                    reason = "requires UTF-8 text; undecodable file" if prefix else "unsupported NUL-bearing content"
                    with self.assertRaisesRegex(validator.ValidationError, reason) as error:
                        validator.check_secrets()
                    self.assertIn("utf16.txt", str(error.exception))
                    self.assertNotIn(fake_token, str(error.exception))

    def test_nul_binary_without_credential_is_rejected(self):
        path = self.root / "nul-binary.dat"
        path.write_bytes(b"unsupported\0binary\n")
        self.track(path)
        with self.assertRaisesRegex(validator.ValidationError, "unsupported NUL-bearing content in 'nul-binary.dat'"):
            validator.check_secrets()

    def test_truncated_utf8_sequence_at_eof_fails(self):
        path = self.root / "truncated.txt"
        path.write_bytes(b"clean text\n\xe2\x82")
        self.track(path)
        with self.assertRaisesRegex(validator.ValidationError, "requires UTF-8 text; undecodable file: 'truncated.txt'"):
            validator.check_secrets()

    def test_unreadable_file_diagnostic_does_not_echo_os_error(self):
        path = self.root / "unreadable.txt"
        path.write_text("clean text\n", encoding="utf-8")
        self.track(path)
        real_open = os.open

        def deny_read(name, *args, **kwargs):
            if name == path.name:
                raise PermissionError("untrusted OS error sentinel")
            return real_open(name, *args, **kwargs)

        # Deterministic even when the suite is run as root; enumeration remains real Git.
        with patch.object(validator.os, "open", side_effect=deny_read):
            with self.assertRaisesRegex(validator.ValidationError, "could not read 'unreadable.txt': PermissionError") as error:
                validator.check_secrets()
        self.assertNotIn("untrusted OS error sentinel", str(error.exception))

    def test_line_reading_is_bounded(self):
        self.track(self.root / "README.md")

        class BoundedText(io.StringIO):
            def read(self, *args, **kwargs):
                raise AssertionError("Unbounded read is forbidden")

            def readline(handle, size=-1):
                self.assertEqual(size, validator.SECRET_SCAN_LINE_LIMIT + 1)
                return super().readline(size)

        with patch.object(validator, "open_security_text", return_value=BoundedText("clean\n")):
            self.assertEqual(validator.check_secrets(), (1, 0))

    def test_utf8_and_secret_boundaries_are_preserved(self):
        path = self.root / "boundaries.txt"
        fake_token = "gh" + "p_" + "A" * 36
        self.track(self.root / "README.md")
        for newline in ("\n", "\r\n", "\r"):
            for prefix in ("", "é" * 4095 + " ", "x" * 8190 + " "):
                with self.subTest(newline=repr(newline), prefix_length=len(prefix)):
                    path.write_bytes(("clean" + newline + prefix + fake_token).encode("utf-8"))
                    with self.assertRaisesRegex(validator.ValidationError, "Possible GitHub token in boundaries.txt line 2"):
                        validator.check_secrets()
        limit = validator.SECRET_SCAN_LINE_LIMIT
        for text in ("é" * limit, "x" * (limit - 1) + "\n"):
            path.write_text(text, encoding="utf-8")
            self.assertEqual(validator.check_secrets(), (2, 0))
        path.write_text("x" * limit + "\n", encoding="utf-8")
        with self.assertRaisesRegex(validator.ValidationError, "line length limit.*boundaries.txt"):
            validator.check_secrets()

    def test_existing_secret_patterns_still_fail_safely(self):
        path = self.root / "patterns.txt"
        self.track(self.root / "README.md")
        for label, token in (
            ("private key", "-----BEGIN " + "PRIVATE KEY-----"),
            ("GitHub token", "gh" + "p_" + "A" * 36),
            ("GitHub fine-grained token", "github_" + "pat_" + "A" * 70),
            ("AWS access key", "AK" + "IA" + "A" * 16),
            ("Google API key", "AI" + "za" + "A" * 35),
            ("Slack token", "xo" + "xb-" + "A" * 20),
            ("OpenAI-style secret key", "s" + "k-" + "A" * 24),
        ):
            with self.subTest(label=label):
                path.write_text(token + "\n", encoding="utf-8")
                with self.assertRaises(validator.ValidationError) as error:
                    validator.check_secrets()
                self.assertIn(f"Possible {label} in patterns.txt", str(error.exception))
                self.assertNotIn(token, str(error.exception))


if __name__ == "__main__":
    unittest.main()
