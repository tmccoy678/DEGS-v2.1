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

    def test_deep_decodable_containers_preserve_existing_comparison_support(self):
        for prefix, suffix in (("[", "]"), ('{"a":', "}")):
            left = json.loads(prefix * 600 + "1" + suffix * 600)
            equal = json.loads(prefix * 600 + "1.0" + suffix * 600)
            different = json.loads(prefix * 600 + "true" + suffix * 600)
            for keyword in ("const", "enum"):
                for operand, expected in ((equal, True), (different, False)):
                    schema = {keyword: [operand] if keyword == "enum" else operand}
                    with self.subTest(kind=prefix, keyword=keyword, expected=expected):
                        self.assertEqual(not GATE.json_schema_errors(left, schema, schema), expected)


if __name__ == "__main__":
    unittest.main()
