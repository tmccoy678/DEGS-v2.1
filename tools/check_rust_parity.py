#!/usr/bin/env python3
"""Compare the exported Python operations with the pinned Rust excerpt oracle.

Run after building tests/rust_reference. Only decoded JSON object inputs are
compared for output structs; Sashiko's whole response extractor is out of scope.
"""
import argparse
from dataclasses import asdict
from copy import deepcopy
import json
from pathlib import Path
import random
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sashiko_derived import (StageConcernsOutput, ConflictResolutionOutput,
                            VerificationOutput, append_stage_items,
                            append_stage_dismissed_concerns)


def cases():
    values = [None, False, True, 0, -1, 1.25, -(2**63), 2**64 - 1,
              "", " ", "évidence", [], [None, {"nested": [1]}], {},
              {"type": "", "stage": "old"}, {"type": "Security"},
              {"type": None}, {"type": False}, {"type": [1]},
              {"reasoning": {"evidence": ["E1"]}}]
    for op, keys in [("stage", ["concerns", "dismissed_concerns"]),
                     ("conflict", ["concerns"]), ("verification", ["findings"])]:
        yield {"op": op, "value": {}}
        yield {"op": op, "value": {"unrecognized": "ignored"}}
        for key in keys:
            for value in values:
                yield {"op": op, "value": {key: value}}
        yield {"op": op, "value": {key: values for key in keys}}
    rng = random.Random(20260911)
    for op in ["dismissed", "positive"]:
        for _ in range(120):
            yield {"op": op, "src": [rng.choice(values) for _ in range(rng.randrange(8))],
                   "dest": [{"existing": [1]}], "stage": rng.choice(["goal", "", "resources", "évidence"])}

        shared = []
        yield {"op": op, "src": [{"left": shared, "right": shared}],
               "dest": [], "stage": "goal", "mutate_left": True}


def python_result(case):
    types = {"stage": StageConcernsOutput, "conflict": ConflictResolutionOutput,
             "verification": VerificationOutput}
    if case["op"] in types:
        try:
            return {"ok": asdict(types[case["op"]].from_mapping(case["value"]))}
        except ValueError:
            return {"error": True}
    # Preserve case-builder aliases here to exercise Python ownership behavior.
    value = deepcopy(case)
    if case["op"] == "dismissed":
        append_stage_dismissed_concerns(value["dest"], value["src"], value["stage"])
    else:
        append_stage_items(value["dest"], value["src"], value["stage"], "General", "description")
    if case.get("mutate_left"):
        value["dest"][-1]["left"].append("changed")
    return {"ok": value["dest"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oracle", required=True, type=Path)
    args = parser.parse_args()
    inputs = list(cases())
    run = subprocess.run([str(args.oracle.resolve())],
                         input="".join(json.dumps(c, allow_nan=False) + "\n" for c in inputs),
                         text=True, capture_output=True, check=True, timeout=30)
    results = run.stdout.splitlines()
    if len(results) != len(inputs):
        raise RuntimeError("oracle result count differs from input count")
    for index, (case, raw) in enumerate(zip(inputs, results)):
        expected = json.dumps(json.loads(raw), sort_keys=True, allow_nan=False)
        actual = json.dumps(python_result(case), sort_keys=True, allow_nan=False)
        if expected != actual:
            raise AssertionError(f"case {index}: {case!r}\nRust={expected}\nPython={actual}")
    print(json.dumps({"result": "PASS", "cases": len(inputs),
                      "seed": 20260911, "scope": "selected value operations and decoded-object outputs"}))


if __name__ == "__main__":
    main()
