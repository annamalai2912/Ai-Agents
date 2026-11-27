# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-27)

---

### 1. [Read-Only Reviewer Role for MCP Server](https://github.com/Sam-AEC/aec-model-bridge/issues/210) — *128 stars*
- **Profile Value:** Contributing to Model Context Protocol (MCP) tooling and CAD/BIM automation bridges demonstrates modern systems engineering, security boundary design, and AI workflow governance.
- **The Challenge:** The MCP server lacks a fine-grained role boundary for monitoring and auditing. We need to introduce an explicit `read_only_reviewer` role that can inspect proposed plans and execution proofs, but is strictly blocked from executing approval mutations or state changes.
- **Technical Plan:**
  1. **Extend Role Definitions (`security/approval.py`)**: Add `ROLE_READ_ONLY_REVIEWER` and update authorization logic so read actions return `True` while approval/mutation actions return `False` or raise a `PermissionError`.
  2. **Enforce Role Guards (`panel_server.py`)**: Inspect MCP tool handlers and ensure approval endpoints explicitly validate caller permissions, returning clean JSON-RPC error responses if unauthorized.
  3. **Mock Mode Support**: Ensure test clients can be provisioned with the new role for local validation.
  4. **Testing**: Add a `pytest` test case in `tests/test_security.py` to verify that read operations succeed while approval attempts are successfully blocked.

- **Ready-to-Post Claim Comment:**
```markdown
Hi maintainers! I’d love to take this on and implement the `read-only reviewer` role. 

**Planned Approach:**
1. Introduce `ROLE_READ_ONLY_REVIEWER` in `security/approval.py` and configure authorization guards so read actions pass while mutation/approval actions raise explicit permission errors.
2. Update MCP tool handlers in `panel_server.py` to intercept unauthorized approval attempts from read-only clients and return clean refusal messages.
3. Add robust unit tests under `tests/` verifying both successful plan/proof inspection and blocked approval behaviors under mock mode.

Please assign this issue to me so I can get started on a pull request!
```

---

### 2. [Optional Two-Person Rule for Plan Approvals](https://github.com/Sam-AEC/aec-model-bridge/issues/203) — *128 stars*
- **Profile Value:** Implementing enterprise compliance and safety governance features like separation of duties highlights a strong grasp of rigorous safety workflows for AI-assisted engineering tools.
- **The Challenge:** Implement an optional two-person rule for plan approvals where the original author of a plan is strictly forbidden from approving their own plan, ensuring compliance and separation of duties.
- **Technical Plan:**
  1. **Update Policy Schema (`policy.py`)**: Add an off-by-default configuration flag for the two-person rule (e.g., `TWO_PERSON_APPROVAL_ENABLED`).
  2. **Capture Author Metadata (`security/approval.py`)**: Ensure plan creation stamps the author's unique identifier (`author_id`) onto the metadata record.
  3. **Enforce Separation of Duties**: Modify approval validation to check if the policy flag is active and block self-approvals (`approver_id == plan.author_id`).
  4. **Propagate Context (`approve_cli.py`)**: Ensure the CLI passes the correct active user context during approval requests.
  5. **Testing**: Add `pytest` test cases verifying both disabled (self-approval allowed) and enabled (self-approval blocked) states.

- **Ready-to-Post Claim Comment:**
```markdown
Hi maintainers! I would like to tackle this feature to implement the optional two-person rule for plan approvals.

**Planned Approach:**
1. Add an off-by-default configuration flag in `policy.py` for the two-person rule.
2. Update plan generation logic in `security/approval.py` to securely stamp the author's identifier onto plan metadata.
3. Implement self-approval interception in the approval workflow, throwing a descriptive exception when the rule is active and an author attempts to approve their own plan.
4. Update `approve_cli.py` to propagate the actor's user context cleanly, and add comprehensive `pytest` coverage for both enabled and disabled states.

Could you please assign this issue to me?
```

---

### 3. [Filter Disabled Dependencies in Release Age Script](https://github.com/renovatebot/renovate/issues/40725) — *23,291 stars*
- **Profile Value:** Committing code to `renovatebot/renovate` instantly adds high-tier open-source prestige to a developer portfolio given its scale and widespread adoption across the global software industry.
- **The Challenge:** The `missingCurrentVersionTimestamps` script currently reports warnings for dependencies even if they are explicitly disabled (`enabled: false`), creating unwanted log noise. We need to filter out disabled packages prior to timestamp validation.
- **Technical Plan:**
  1. **Locate Target Utility**: Find the script/module implementing `missingCurrentVersionTimestamps`.
  2. **Apply `enabled` Filter**: Update the dependency iteration logic to filter out any package where `enabled` explicitly evaluates to `false` (taking care not to drop packages where `enabled` is undefined, as they default to `true`).
  3. **Respect Config Scoping**: Verify that package-specific and global rules are correctly honored during the filtering step.
  4. **Testing**: Add a Jest unit test fixture containing mixed dependencies (enabled vs. disabled with missing timestamps) to verify that disabled packages are successfully ignored.

- **Ready-to-Post Claim Comment:**
```markdown
Hi maintainers! I'd love to help clean up this diagnostic warning by filtering out disabled dependencies in the release age script.

**Planned Approach:**
1. Locate the `missingCurrentVersionTimestamps` helper script within the codebase.
2. Refactor the dependency collection/filtering step to explicitly exclude packages configured with `enabled: false`, safely preserving default undefined behaviors.
3. Add a Jest unit test case covering mixed enabled/disabled fixtures to ensure disabled dependencies no longer trigger spurious warnings.

Please assign this issue to me so I can open a PR!
```