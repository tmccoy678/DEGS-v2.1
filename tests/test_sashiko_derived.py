import unittest

from sashiko_derived import append_stage_dismissed_concerns, append_stage_items, StageConcernsOutput, ConflictResolutionOutput, VerificationOutput, ReviewState


class SourcePortTests(unittest.TestCase):
    def test_append_preserves_order_scalars_and_detaches_nested_values(self):
        original = [{"stage": "earlier", "reasoning": {"evidence": ["E1"]}}, 7, None]
        dest = [{"existing": True}]
        append_stage_dismissed_concerns(dest, original, "resources")
        self.assertEqual(dest, [{"existing": True}, {"stage": "resources", "reasoning": {"evidence": ["E1"]}}, 7, None])
        dest[1]["reasoning"]["evidence"].append("E2")
        self.assertEqual(original[0], {"stage": "earlier", "reasoning": {"evidence": ["E1"]}})

    def test_positive_items_default_only_missing_nonstring_or_empty_type(self):
        dest = []
        src = [{}, {"type": ""}, {"type": None}, {"type": False}, {"type": " "}, {"type": "Security", "stage": "old"}, "scalar"]
        append_stage_items(dest, src, "security", "General", "description")
        self.assertEqual([x["type"] for x in dest[:-1]], ["General", "General", "General", "General", " ", "Security"])
        self.assertEqual(dest[-1], "scalar")
        self.assertEqual(dest[-2]["stage"], "security")
        self.assertEqual(src[0], {})

    def test_object_boundary_defaults_rejects_wrong_fields_and_ignores_extras(self):
        self.assertEqual(StageConcernsOutput.from_mapping({"extra": 1}).concerns, [])
        for invalid in [None, 1, "", {}, False]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    StageConcernsOutput.from_mapping({"concerns": invalid})
        source = {"dismissed_concerns": [None, 5, {"reasoning": ["E1"]}]}
        value = StageConcernsOutput.from_mapping(source)
        value.dismissed_concerns[-1]["reasoning"].append("E2")
        self.assertEqual(source["dismissed_concerns"][-1]["reasoning"], ["E1"])
        self.assertEqual(ConflictResolutionOutput.from_mapping({}).concerns, [])
        self.assertEqual(VerificationOutput.from_mapping({}).findings, [])
        with self.assertRaises(ValueError):
            VerificationOutput.from_mapping({"findings": None})
        with self.assertRaises(ValueError):
            StageConcernsOutput.from_mapping([])

    def test_state_defaults_are_independent(self):
        a, b = ReviewState(), ReviewState()
        a.all_concerns.append({"description": "candidate"})
        self.assertEqual(b.all_concerns, [])
        self.assertEqual(a.all_dismissed_concerns, [])
        self.assertEqual(a.deduplicated_concerns, [])
        self.assertEqual(a.deduplicated_dismissed_concerns, [])
        self.assertEqual(a.conflict_resolved_concerns, [])
        self.assertEqual(a.findings, [])
        x, y = StageConcernsOutput(), StageConcernsOutput()
        x.concerns.append(1)
        self.assertEqual(y.concerns, [])
        self.assertEqual(x.dismissed_concerns, [])

    def test_aliasing_is_rejected_before_any_append(self):
        values = []
        with self.assertRaises(ValueError):
            append_stage_dismissed_concerns(values, values, "goal")
        with self.assertRaises(ValueError):
            append_stage_items(values, values, "goal", "General", "description")

    def test_shared_python_subtrees_become_independent_owned_json_subtrees(self):
        shared = []
        source = [{"left": shared, "right": shared}]
        for append in [
            lambda dest: append_stage_dismissed_concerns(dest, source, "goal"),
            lambda dest: append_stage_items(dest, source, "goal", "General", "description"),
        ]:
            dest = []
            append(dest)
            dest[0]["left"].append("changed")
            self.assertEqual(dest[0]["right"], [])
            self.assertEqual(shared, [])
        output = StageConcernsOutput.from_mapping({"concerns": source})
        output.concerns[0]["left"].append("changed")
        self.assertEqual(output.concerns[0]["right"], [])
        self.assertEqual(shared, [])


if __name__ == "__main__":
    unittest.main()
