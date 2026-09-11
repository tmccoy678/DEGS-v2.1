# Copyright 2026 The Sashiko Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Modified for DobeWorks/DEGS: selected Rust operations translated to Python.
# Object-only adapter and alias guard are documented Python adaptations.
# Source ranges and hashes: provenance/sashiko-source.json

"""Selected Sashiko value operations; no semantic review or authority decisions."""

from copy import deepcopy
from dataclasses import dataclass, field
from typing import Any


def append_stage_dismissed_concerns(dest, src, stage):
    """Append detached JSON values; stamp objects with the producing stage.

    Inputs are JSON-compatible values; dest and src must be distinct lists,
    corresponding to Rust's exclusive mutable destination borrow.
    """
    if dest is src:
        raise ValueError("source and destination must be distinct lists")
    for item in src:
        obj = deepcopy(item)
        if isinstance(obj, dict):
            obj["stage"] = stage
        dest.append(obj)


def append_stage_items(dest, src, stage, default_type, _key):
    """Port of upstream lines 396-419; the upstream key argument is unused."""
    if dest is src:
        raise ValueError("source and destination must be distinct lists")
    for item in src:
        obj = deepcopy(item)
        if isinstance(obj, dict):
            value = obj.get("type")
            if not isinstance(value, str) or not value:
                obj["type"] = default_type
            obj["stage"] = stage
        dest.append(obj)


def _array(payload, name):
    if not isinstance(payload, dict):
        raise ValueError("stage output must be a decoded JSON object")
    value = payload.get(name, [])
    if not isinstance(value, list):
        raise ValueError(name + " must be an array; null is not an omitted field")
    return deepcopy(value)


@dataclass
class StageConcernsOutput:
    """Selected source lines 92-98; from_mapping is an object-only adapter.

    This is not Sashiko's complete response extractor or a JSON text parser.
    Values must already be finite, acyclic, JSON-compatible data.
    """
    concerns: list[Any] = field(default_factory=list)
    dismissed_concerns: list[Any] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, payload):
        return cls(_array(payload, "concerns"), _array(payload, "dismissed_concerns"))


@dataclass
class ConflictResolutionOutput:
    """Selected source lines 100-104."""
    concerns: list[Any] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, payload):
        return cls(_array(payload, "concerns"))


@dataclass
class VerificationOutput:
    """Selected source lines 106-110."""
    findings: list[Any] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, payload):
        return cls(_array(payload, "findings"))


@dataclass
class ReviewState:
    """Extracted fields 56-70, not the complete upstream KernelReviewState."""
    all_concerns: list[Any] = field(default_factory=list)
    all_dismissed_concerns: list[Any] = field(default_factory=list)
    deduplicated_concerns: list[Any] = field(default_factory=list)
    deduplicated_dismissed_concerns: list[Any] = field(default_factory=list)
    conflict_resolved_concerns: list[Any] = field(default_factory=list)
    findings: list[Any] = field(default_factory=list)
