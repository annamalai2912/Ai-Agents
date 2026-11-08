# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-08)

- ### [btclib-org/bip32-descriptors #133: miniscript.parse quotes an unknown context it was given in its refusal](https://github.com/btclib-org/bip32-descriptors/issues/133) (9 ⭐)
- **Profile Value:** Showcases advanced security mindfulness in cryptographic and Bitcoin-focused Python libraries by preventing side-channel leaks and sensitive data exposure in error messages.
- **The Challenge:** When parsing invalid or malformed descriptors with unknown contexts, `_assert_valid_context` currently echoes the raw user-supplied context string back into the exception, violating the security invariant: *"A refusal carries no secret"*.
- **Technical Plan:** 
  1. Inspect `src/bip32_descriptors/descriptors/miniscript.py` and locate `_assert_valid_context`.
  2. Rewrite the exception formatting to omit the raw `context` input and instead display only the expected valid options.
  3. Add a unit test (`test_miniscript_parse_unknown_context_no_leak`) in `tests/descriptors/test_miniscript.py` asserting that arbitrary/secret strings passed as contexts do not appear in the raised exception message.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to tackle this issue. 

  I plan to update `_assert_valid_context` in `src/bip32_descriptors/descriptors/miniscript.py` to ensure that unknown user-provided contexts are no longer echoed back in exception messages (upholding the *"A refusal carries no secret"* invariant). I'll also add a dedicated regression test with `pytest` to guarantee secrets/arbitrary context strings never leak through parse errors.

  Please let me know if this approach sounds good and if you can assign this issue to me!
  ```

---

- ### [luciano2-web/Luciano-Sarmiento #28: 🧪 tests: ampliar pruebas del sistema de personalidad (src/core/personality.py)](https://github.com/luciano2-web/Luciano-Sarmiento/issues/28) (1 ⭐)
- **Profile Value:** Demonstrates strong test-driven development (TDD) skills and robust unit-testing patterns (`pytest`) for AI agentic guardrails and conversational constraints.
- **The Challenge:** Broaden test coverage in `tests/test_personality.py` for `src/core/personality.py` to rigorously validate tone stability, phrase limits, and forbidden keyword filtering (e.g., "AI", "ChatGPT") without relying on external LLM APIs.
- **Technical Plan:** 
  1. Review the core methods inside `src/core/personality.py`.
  2. Expand `tests/test_personality.py` to include tests covering forbidden keyword detection/sanitization, system prompt persona consistency (Félix the cat coder), and edge-case inputs (empty strings, special characters, code snippets).
  3. Run `pytest tests/test_personality.py -v` to ensure green status.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi team! I would like to help expand the test suite for the personality system.

  My plan is to add comprehensive unit tests to `tests/test_personality.py` covering forbidden keyword filtering, persona system prompt validation, and edge-case string handling as outlined in the issue description. This will ensure robust guardrail enforcement without external API dependencies.

  Could you please assign this issue to me? Ready to get started!
  ```