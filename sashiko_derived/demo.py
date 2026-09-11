"""Synthetic accumulation demonstration; no LLM investigation is performed."""
from dataclasses import asdict
import json

from . import ReviewState, StageConcernsOutput, append_stage_items, append_stage_dismissed_concerns


def main():
    state = ReviewState()
    output = StageConcernsOutput.from_mapping({
        "concerns": [{"description": "Synthetic candidate: missing cleanup", "type": "Resources"}],
        "dismissed_concerns": [{"description": "Synthetic candidate: missing cleanup",
                                 "reasoning": "Illustrative supplied counterevidence; not independently verified.",
                                 "locations": []}],
    })
    append_stage_items(state.all_concerns, output.concerns, "resources", "General", "description")
    append_stage_dismissed_concerns(state.all_dismissed_concerns, output.dismissed_concerns, "resources")
    print(json.dumps({"demonstration": "synthetic accumulation only", "state": asdict(state)}, indent=2))


if __name__ == "__main__":
    main()
