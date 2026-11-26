# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-26)

- ### [adobe/react-spectrum #10310](https://github.com/adobe/react-spectrum/issues/10310) (16,069 ⭐)
- **Profile Value:** Mastering cross-browser event handling and accessibility edge cases in industry-leading design systems proves your enterprise-grade frontend engineering competence.
- **The Challenge:** In Chromium browsers, screen readers (JAWS/NVDA) trigger synthetic `pointerdown` events with `pointerType: "mouse"` during virtual cursor navigation, causing `useInteractionModality` to incorrectly drop keyboard/screen reader focus rings.
- **Technical Plan:**
  1. Inspect `packages/@react-aria/interactions/src/useInteractionModality.ts` to analyze event listener triggers.
  2. Implement coordinate heuristic checks (`clientX === 0 && clientY === 0`) on `pointerdown` events with `pointerType: 'mouse'` to filter out virtual screen reader artifacts.
  3. Ensure genuine top-left corner clicks and non-Chromium browsers remain unaffected.
  4. Write unit tests covering synthetic vs. genuine pointer events in `useInteractionModality.test.ts`.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to tackle this issue. I've analyzed the problem domain and plan to introduce a coordinate heuristic check (`clientX`/`clientY` validation) in `useInteractionModality.ts` to correctly filter out synthetic `pointerType: 'mouse'` events fired by screen readers in Chromium without impacting genuine user interactions. 

  Could you please assign this issue to me? I'll have a robust PR ready with unit tests soon!
  ```

---

- ### [suiramdev/freenary #358](https://github.com/suiramdev/freenary/issues/358) (3 ⭐)
- **Profile Value:** Demonstrating clean full-stack TypeScript execution by adding localized API responses and robust backend unit testing adds strong versatility to your portfolio.
- **The Challenge:** The mock bank consent page currently renders hardcoded English text and metadata without accepting or validating internationalization (`locale`) parameters.
- **Technical Plan:**
  1. Define a supported locales constant list and fallback default (`'en'`) in the mock bank module.
  2. Update the consent route controller to extract, sanitize, and validate the `locale` search parameter from incoming requests.
  3. Inject the correct translation dictionaries and update HTML metadata/content (including `<html lang="...">`).
  4. Implement integration/unit tests covering valid, invalid/malicious, and missing locale parameters.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hello! I would love to pick up this issue. My plan is to add dynamic locale parameter extraction to the mock bank consent route, validate inputs against a supported locales whitelist with a clean fallback to English, and add comprehensive test coverage in `consent.test.ts`.

  Please assign this to me when you have a moment. Thanks!
  ```

---

- ### [ranjeetds/hackfloor #17](https://github.com/ranjeetds/hackfloor/issues/17) (0 ⭐)
- **Profile Value:** Building security reporting infrastructure and integrating with GitHub's native CodeQL/SARIF workflows showcases high-value DevSecOps and AI agent engineering capabilities.
- **The Challenge:** Hackfloor lacks a SARIF output format, preventing security findings and guardrail alerts from being natively ingested by GitHub's Code Scanning dashboard.
- **Technical Plan:**
  1. Map Hackfloor's findings data model to the SARIF v2.1.0 specification schema (`$schema`, `version`, `runs`, `results`, `locations`).
  2. Build a new `SarifReporter` module that transforms raw evaluation results and maps internal severities to standard SARIF levels (`error`, `warning`, `note`).
  3. Expose a CLI output flag (e.g., `--format sarif`) for seamless local and CI pipeline usage.
  4. Write unit tests validating generated JSON against the official SARIF v2.1.0 schema.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi @ranjeetds, I would love to implement SARIF output for Hackfloor! I plan to build a dedicated reporter mapping results to the SARIF v2.1.0 specification, expose a `--format sarif` CLI flag, and include schema validation unit tests to ensure seamless GitHub Code Scanning integration.

  Could you please assign this issue to me? Excited to contribute!
  ```