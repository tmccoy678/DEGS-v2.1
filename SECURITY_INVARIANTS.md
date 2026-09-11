# Dobeworks EGS Security Invariants

These invariants are local safety boundaries. They are normative through the cited Engineering Charter rules and remain in force throughout the policy lifecycle, including while DEGS is ACTIVE.

| Invariant | Governing rule |
|---|---|
| PRIVATE VAULT remains outside all agent authority. | `DEGS-SEC-003` |
| Governance artifacts contain no secret values. | `DEGS-SEC-002` |
| AgentOps remains non-admin unless explicitly redesigned and audited. | `DEGS-AI-004` |
| No backup deletion occurs without recovery validation. | `DEGS-DATA-001` |
| No 2015 MacBook Pro wipe occurs without a validated backup and explicit approval. | `DEGS-DATA-001`, `DEGS-RISK-003` |
| No Seagate mutation occurs during a read-only audit. | `DEGS-CFG-001`, `DEGS-DATA-001` |
| FileVault, SIP, and Gatekeeper remain enabled and unweakened. | `DEGS-SEC-004` |
| Arbitrary passwordless root is prohibited. | `DEGS-SEC-005` |
| High-consequence filesystem, command, egress, dependency, secret, and approval boundaries are deterministic and enforced outside the model; prompt-only or unknown control state blocks. | `DEGS-SEC-006` |
| Agents do not self-escalate. | `DEGS-AI-003` |
| Independent review receives no silent provider or model substitution. | `DEGS-AI-002` |
| Consequential AI work records intended and unsupported uses, affected stakeholders, human control, whole-system tests, limits, monitoring, and retirement; Taylor retains the decision. | `DEGS-AI-006` |
| Normal startup performs no paid health request. | `DEGS-OPS-002`, `DEGS-OPS-004` |
| No destructive decision relies only on apparent or logical storage size. | `DEGS-DATA-002` |
| Data use has an explicit purpose, owner, minimum-necessary field set, provenance, authority, retention boundary, and separately evidenced repurposing authority. | `DEGS-DATA-003` |
| Tier 3 hazards are eliminated or mitigated and tested; any residual-risk acceptance is Taylor's separate HUMAN out-of-band decision with evidence. | `DEGS-RISK-006` |
| Completion is never claimed without applicable evidence. | `DEGS-OPS-001` |
| Controlled state has no duplicate active source of truth. | `DEGS-CFG-002`, `DEGS-CFG-003` |
| Governance work makes no unrelated filesystem mutation. | `DEGS-REQ-001`, `DEGS-CFG-001` |

Any observed contradiction is drift. Security drift stops the operation; material or unknown drift requires review before proceeding.
