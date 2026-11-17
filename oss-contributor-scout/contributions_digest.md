# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-17)

---

### 1. WebsiteBench: Fix Time Budget Key Lookup
* **Repo & Issue:** [TIGER-AI-Lab/WebsiteBench #49](https://github.com/TIGER-AI-Lab/WebsiteBench/issues/49) — *Case time budget looks up `check_id`, but T3 cases carry `cicd_check_id`*
* **Repo Stars:** ~494 stars
* **Profile Value:** Contributing to an advanced AI agent evaluation framework demonstrates your ability to troubleshoot complex benchmark runtimes, harness validation bugs, and metric configurations.
* **The Challenge:** T3-tier cases carry their identifiers under `cicd_check_id` instead of `check_id`, causing a lookup miss that silently falls back to an incorrect default timeout budget (~780s instead of ~6,124s).
* **Technical Plan:**
  1. Inspect `websitebench/evaluation/formal.py` around lines 827–831 where the budget dictionary lookup is performed.
  2. Implement conditional key resolution to check for `cicd_check_id` first, falling back to `check_id`.
  3. Write a dedicated unit test in `tests/test_formal.py` verifying correct budget allocation for both standard and T3 cases.
  4. Run pytest via `poetry run pytest tests/test_formal.py` to ensure all tests pass.
* **Ready-to-Post Claim Comment:**
```markdown
Hi maintainers! I'd love to tackle this issue. 

I've reviewed `websitebench/evaluation/formal.py` (specifically lines ~827-831) and can confirm the dictionary lookup logic needs to check for `cicd_check_id` when evaluating T3 cases to prevent the silent fallback to default timeouts. 

**Proposed Approach:**
1. Update the budget lookup in `formal.py` to dynamically resolve keys based on whether `cicd_check_id` is present.
2. Add a robust unit test in `tests/test_formal.py` that validates both standard and T3 case budget resolutions.
3. Verify via `poetry run pytest`.

Could you please assign this issue to me? I'm ready to submit a PR!
```

---

### 2. OphirPay: Display Gas Fee Estimation Spinner
* **Repo & Issue:** [OphirPay/OphirPay #1915](https://github.com/OphirPay/OphirPay/issues/1915) — *feat(ui): display gas fee estimation spinner during on-chain payment simulation*
* **Repo Stars:** 5 stars (Active Stellar/Soroban Web3 dashboard)
* **Profile Value:** Merging a frontend UX enhancement into a Web3 dashboard showcases your proficiency with React state management, async RPC simulations, and user feedback loops.
* **The Challenge:** During on-chain payment simulations, gas fee estimation can take several seconds without visual feedback, and the submit button remains active during calculation.
* **Technical Plan:**
  1. Destructure the `isSimulating` boolean state from the gas estimation hook in `src/components/payment/PaymentForm.tsx`.
  2. Conditionally render an inline loading spinner adjacent to the fee estimate label when `isSimulating` is true.
  3. Disable the submit button (`disabled={isSimulating || !isValid}`) during active simulation to prevent race conditions.
  4. Write component tests using React Testing Library and verify behavior locally via `pnpm dev`.
* **Ready-to-Post Claim Comment:**
```markdown
Hello! I would love to pick up this "Good First Issue". 

**Proposed Approach:**
1. Destructure `isSimulating` from the gas estimation hook inside `PaymentForm.tsx`.
2. Conditionally render an inline loading spinner next to the fee label when simulation is active.
3. Bind the submit button's `disabled` state to `isSimulating` to prevent duplicate submissions during RPC calculations.
4. Add a quick test to verify spinner presence and button disablement.

Please assign this to me when you have a moment. Thanks!
```

---

### 3. e2e: Bring Missing APIs to e2e (Umbrella Issue)
* **Repo & Issue:** [e2e-inc/e2e #1855](https://github.com/e2e-inc/e2e/issues/1855) — *☂️ Help us bring missing APIs to e2e*
* **Repo Stars:** ~13,970 stars
* **Profile Value:** Contributing code to a high-visibility, 14k+ star testing infrastructure library proves your mastery of cross-platform testing architecture, TypeScript tooling, and strict workspace workflows.
* **The Challenge:** Several missing helper APIs and assertions need implementation to ease user migration from Playwright, Cypress, or Vitest.
* **Technical Plan:**
  1. Select an unassigned missing API sub-task from the umbrella issue catalog (#1855).
  2. Implement TypeScript type definitions and core runner methods inside `packages/e2e/src/`.
  3. Write comprehensive integration/unit tests under `packages/e2e/test/`.
  4. Generate a workspace changeset (`pnpm changeset`), run `pnpm lint` / `oxlint`, and execute the test suite (`pnpm test`).
* **Ready-to-Post Claim Comment:**
```markdown
Hi maintainers! I'd love to contribute by implementing one of the missing APIs tracked in this umbrella issue. 

I'm comfortable working with the codebase's TypeScript structure, strict linters, and changeset workflows. 

**Proposed Approach:**
1. Select an unassigned API feature from the #1855 checklist.
2. Implement the required types and core logic in `packages/e2e/src/`.
3. Add thorough unit/integration tests to guarantee correctness and prevent regressions.
4. Run `pnpm changeset`, verify formatting/linting, and open a clean PR.

Could you please assign this to me and let me know if there's a specific missing API from the list you'd prefer I start with? Thank you!
```