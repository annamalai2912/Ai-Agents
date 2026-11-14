# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-14)

---

### [Nano-Collective/nanocoder — Issue #2194](https://github.com/Nano-Collective/nanocoder/issues/2194) (~2,570 stars)

- **Profile Value:** Fixing local file operations and git integration edge cases in a high-visibility AI coding agent demonstrates your ability to write resilient TypeScript code handling cross-platform filesystem quirks.
- **The Challenge:** Git diff commands quote or escape non-ASCII file paths by default, causing `nanocoder` to skip files with non-ASCII characters (e.g., `café.txt`) during checkpointing and state tracking.
- **Technical Plan:**
  1. Inspect `src/utils/git.ts` and `src/agent/checkpoint.ts` to locate subprocess execution for `git diff --name-only`.
  2. Update the Git command arguments to include `-c core.quotePath=false` (or use `-z` for null-terminated output parsing).
  3. Ensure downstream file path normalization correctly handles UTF-8 characters without octal escape interference.
  4. Write an automated integration/unit test verifying that files with non-ASCII names are correctly captured in checkpoint diffs.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to tackle this issue. 

  I've investigated the root cause: by default, Git escapes non-ASCII characters in path outputs during `git diff --name-only`, causing path mismatches in the TypeScript code. 

  **Proposed fix:**
  1. Update git subprocess execution flags to include `-c core.quotePath=false` (or switch to `-z` for null-delimited path parsing).
  2. Ensure UTF-8 path normalization is preserved across diff parsers.
  3. Add a robust test case in `src/__tests__/git.test.ts` covering non-ASCII file names (e.g., `café.txt`).

  Please assign this issue to me so I can open a pull request!
  ```

---

### [tanveer-arch/promptdrift — Issue #62](https://github.com/tanveer-arch/promptdrift/issues/62) (4 stars)

- **Profile Value:** Showcases your attention to data privacy, robust error handling, and pythonic warning architecture in modern LLM testing applications.
- **The Challenge:** Redaction failures (such as invalid regex patterns or failing custom callbacks) are currently silently swallowed using `pass`, creating a security and debugging blind spot.
- **Technical Plan:**
  1. Define a custom warning class `RedactionWarning(UserWarning)` in `src/promptdrift/exceptions.py`.
  2. Locate the redaction execution block in `src/promptdrift/capture/redaction.py`.
  3. Replace the silent `pass` in `try...except` blocks with `warnings.warn()` while safely returning the original unredacted text for backward compatibility.
  4. Add unit tests using `pytest.warns()` in `tests/test_redaction.py`.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hello! I would like to pick up this issue. 

  **Proposed approach:**
  1. Introduce a custom `RedactionWarning(UserWarning)` subclass in `src/promptdrift/exceptions.py`.
  2. Replace broad `except` blocks swallowing redaction errors with `warnings.warn(..., RedactionWarning)` while maintaining fallback behavior (returning the original string).
  3. Add unit tests using `pytest.warns()` to verify proper warning emission and fallback handling.

  Could you please assign this to me?
  ```

---

### [tanveer-arch/promptdrift — Issue #61](https://github.com/tanveer-arch/promptdrift/issues/61) (4 stars)

- **Profile Value:** Highlights your capability to design clean Pydantic data models and extend evaluation pipelines in production Python test harnesses.
- **The Challenge:** The evaluation module lacks multi-value assertion types (`contains_all` and `contains_any`), which are frequently needed to verify compliance disclaimers or required keyword sets in LLM outputs.
- **Technical Plan:**
  1. Update Pydantic assertion models in `src/promptdrift/models/test.py` to support list-based inputs for `contains_all` and `contains_any`.
  2. Implement evaluation dispatch logic inside `src/promptdrift/evaluators/deterministic.py` for both new assertion types.
  3. Ensure `EvaluationResult.reason` returns precise, informative details regarding which items matched or failed.
  4. Write comprehensive unit test coverage in `tests/evaluators/test_deterministic.py`.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to implement `contains_all` and `contains_any` assertion types for the evaluation engine.

  **Proposed approach:**
  1. Update `AssertionConfig` models in `src/promptdrift/models/test.py` to accept list values for the new assertion types.
  2. Implement validation and check logic in `src/promptdrift/evaluators/deterministic.py` with clear, informative failure reasons.
  3. Add a thorough parameterized test suite in `tests/evaluators/test_deterministic.py` covering passing and failing states.

  Please assign this issue to me so I can get started!
  ```