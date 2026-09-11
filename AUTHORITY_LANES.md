# Dobeworks EGS Authority Lanes

Authority selection is governed by `DEGS-AI-001` through `DEGS-AI-005`. A lane describes who may decide or act; it does not grant new permission.

## Command Center

- architecture;
- research;
- planning;
- independent audit; and
- read-mostly work.

## Taylor AI Workbench

- supervised local implementation;
- bounded workspace changes; and
- configuration work with explicit verification.

## AgentOps

- deliberately delegated autonomous work;
- separate non-administrator operating-system identity; and
- no automatic privilege increase.

AgentOps authority is bounded by `DEGS-AI-003` and `DEGS-AI-004`. Delegation does not include credentials, physical action, destructive approval, governance activation, or governance exceptions.

## Taylor

- credentials;
- authentication;
- destructive approval;
- physical actions;
- value judgments; and
- approval of governance activation and exceptions.

## PRIVATE VAULT

PRIVATE VAULT is outside all agent authority under `DEGS-SEC-003`.

No agent may reinterpret inconvenience as permission to increase its authority.

## Evaluation and context-routing scopes

**Task-record evaluation scope:** the engineering gate may evaluate a human `TAYLOR` task record at Tier 1 or Tier 2. This recognizes Taylor's direct human authority; it does not route an agent, authorize execution, or bypass evidence controls.

**Phase-boundary context-routing scope:** `context-governance.py` routes Tier 1 and Tier 2 continuation to `TAYLOR_AI_WORKBENCH` or deliberately delegated `AGENTOPS`, and reserves the `TAYLOR` route for Tier 3 human decisions. This stricter routing prevents a context handoff from recasting supervised agent work as direct human action.

The two maps answer different questions and therefore intentionally differ. Neither map authenticates Taylor or grants activation, execution, credential, destructive, or physical-action authority.
