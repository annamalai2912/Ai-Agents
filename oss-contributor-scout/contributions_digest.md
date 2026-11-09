# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-09)

---

### ### [Correct formatting of the sample TOC on the Edition edit page](https://github.com/internetarchive/openlibrary/issues/14322) (Repo Stars: ~6,817)
- **Profile Value:** Contributing code to the Internet Archive's Open Library adds a globally recognized, high-scale digital library project to your portfolio, proving your ability to collaborate on massive, production-grade repositories.
- **The Challenge:** The Table of Contents (TOC) sample formatting on the Edition edit page does not render correctly according to standard specifications or layout requirements.
- **Technical Plan:**
  1. Search the codebase for bindings related to the TOC input field (`id="id_table_of_contents"` or similar) under `openlibrary/templates/edition/`.
  2. Inspect whether the rendering breakdown is caused by missing HTML preformatting tags, template filters, or CSS rules.
  3. Apply the appropriate fix—such as adding `white-space: pre-wrap;` to the preview container or adjusting template output handling.
  4. Spin up the local dev instance, input a multi-line TOC sample, and verify that the layout matches the issue's reference screenshots.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I would love to pick up this issue and submit a fix for the TOC sample formatting on the Edition edit page. 

  **Planned Approach:**
  1. Locate the relevant template files under `openlibrary/templates/edition/` and styling rules targeting the TOC preview container.
  2. Investigate the whitespace and newline rendering behavior causing the layout breakdown.
  3. Apply the correct CSS or templating fix (e.g., ensuring `white-space: pre-wrap` or proper escaping is used).
  4. Test locally to ensure multi-line TOC previews render accurately across views.

  Could you please assign this issue to me? Thank you!
  ```

---

### ### [install.sh: on Linux, point to the Linux issue](https://github.com/Hadeva-Dev/dawnmere/issues/23) (Repo Stars: 1)
- **Profile Value:** Demonstrating contributions to modern repositories utilizing Model Context Protocol and automated testing frameworks proves your versatility with contemporary CLI tools and script engineering.
- **The Challenge:** The installation shell script (`install.sh`) currently lacks a user-facing informational prompt directing Linux users to the specific Linux tracking issue.
- **Technical Plan:**
  1. Open `install.sh` and locate the platform detection logic utilizing `uname -s`.
  2. Update the Linux branch (`Linux*`) to echo a clear, helpful message pointing users to the designated Linux issue URL.
  3. Inspect `cli/tests/test_install_sh.py` to understand how the shell script execution is currently mocked and tested.
  4. Add a test assertion to `cli/tests/test_install_sh.py` verifying that Linux environments correctly trigger and output the expected issue guidance message.
  5. Run `poetry run pytest cli/tests/test_install_sh.py` to ensure all tests pass successfully.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi there! I'd like to tackle this issue. 

  **Proposed Solution:**
  1. Modify `install.sh` within the Linux platform detection block to output an informative message directing users to the Linux tracking issue URL.
  2. Update the corresponding unit tests in `cli/tests/test_install_sh.py` to assert that the correct Linux notice string is outputted to `stdout` under a simulated Linux environment.
  3. Validate the changes locally using `pytest`.

  Please assign this issue to me if it's still available. Thanks!
  ```