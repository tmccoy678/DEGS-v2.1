"""JSON equality regressions through the existing schema validation seam."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("gate", ROOT / "bin/engineering-gate.py")
GATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GATE)


class JsonEqualityTests(unittest.TestCase):
    def assert_matches(self, left, right, expected):
        for keyword, operand in (("const", right), ("enum", [right])):
            schema = {keyword: operand}
            with self.subTest(left=left, right=right, keyword=keyword):
                self.assertEqual(not GATE.json_schema_errors(left, schema, schema), expected)

    def test_nested_values_follow_json_equality(self):
        cases = [
            ([False], [0], False), ([True], [1], False),
            ({"a": [False]}, {"a": [0]}, False),
            ([{"a": [1, {"b": True}]}], [{"a": [1.0, {"b": 1}]}], False),
            (False, 0, False), (True, 1, False),
            ([1, {"a": 2}], [1.0, {"a": 2.0}], True),
            ({"a": 1, "b": [None]}, {"b": [None], "a": 1.0}, True),
            ({"a": 1}, {"a": 1, "b": 2}, False),
            ([1, 2], [2, 1], False), ([1], [1, 2], False),
            ([], {}, False), ([], [], True), ({}, {}, True),
            ("1", 1, False), (None, None, True), (None, False, False),
            ([True, False], [True, False], True), ("same", "same", True),
            ("same", "different", False), (0, -0.0, True),
        ]
        for left, right, expected in cases:
            self.assert_matches(left, right, expected)
            self.assert_matches(right, left, expected)

    def test_all_fourteen_original_public_failures(self):
        cases = {"enum.json": [(6, 1), (6, 2), (8, 1), (8, 2), (10, 0), (12, 0)],
                 "const.json": [(6, 1), (6, 2), (7, 1), (7, 2), (8, 1), (8, 2), (9, 1), (9, 2)]}
        for filename, indices in cases.items():
            groups = json.loads((ROOT / "benchmarks/data" / filename).read_text())
            for group_index, test_index in indices:
                group = groups[group_index]
                test = group["tests"][test_index]
                with self.subTest(case=f"{filename}:{group_index}:{test_index}"):
                    self.assertIs(test["valid"], False)
                    self.assertTrue(GATE.json_schema_errors(test["data"], group["schema"], group["schema"]))


if __name__ == "__main__":
    unittest.main()
