# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-18)

- ### [Filter runs by model name: `runs list --model` and dashboard `?model=` (#149)](https://github.com/lakshaychhaba0001-sys/openbench-ai/issues/149) · ⭐ 1
- **Profile Value:** Demonstrates full-stack execution capability by cleanly threading query filters across the core business logic, CLI argument parsers, and web HTTP routes while safely guarding against XSS vulnerabilities.
- **The Challenge:** The CLI (`runs list`) and web dashboard currently fetch all benchmarking runs without filtering capabilities. Users need the ability to filter runs by model name both via CLI flag (`--model`) and web query parameter (`?model=`), complete with proper HTML escaping.
- **Technical Plan:**
  1. Extend `ExperimentManager.list_runs` in `src/openbench/core.py` to accept an optional `model` filter parameter.
  2. Update the CLI subparser in `src/openbench/cli.py` to parse `--model` and pass it to the core manager.
  3. Modify `src/openbench/serve.py` to extract the `?model=` query parameter, apply the filter, and use `html.escape()` on all rendered template inputs to prevent XSS.
  4. Write unit tests for core filtering, CLI parsing, and web output safety.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to take this issue. 

  My plan is to:
  1. Update `ExperimentManager.list_runs` in `src/openbench/core.py` to accept and apply a `model` filter.
  2. Wire up the `--model` flag in `src/openbench/cli.py`.
  3. Update `src/openbench/serve.py` to parse the `?model=` query string parameter and ensure safe output rendering via HTML escaping to prevent XSS.
  4. Add unit and integration tests covering core, CLI, and web dashboard filtering.

  Please assign this to me if this approach sounds good!
  ```

---

- ### [`dataset-stats`: add a Markdown format (#147)](https://github.com/lakshaychhaba0001-sys/openbench-ai/issues/147) · ⭐ 1
- **Profile Value:** Highlights precision in developer tooling and documentation maintenance by implementing robust string sanitization for markdown table cells and updating generated reference docs.
- **The Challenge:** The `dataset-stats` command lacks a Markdown output option. Adding `--format markdown` requires producing clean GitHub-flavored tables while safely escaping edge-case characters like pipes (`|`) and newlines (`\n`) using `escape_markdown_cell`.
- **Technical Plan:**
  1. Inspect and import `escape_markdown_cell` into `src/openbench/cli.py`.
  2. Add a `--format` flag supporting `markdown` to the `dataset-stats` CLI command.
  3. Construct a GitHub-flavored Markdown table for dataset statistics, piping all cell values through `escape_markdown_cell`.
  4. Run `python scripts/generate_reference_docs.py` to regenerate the documentation reference.
  5. Add pytest coverage using `tmp_path` fixtures with edge-case dataset strings containing pipes and newlines.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hello! I would like to work on adding the Markdown output format to `dataset-stats`.

  Here is my planned implementation:
  1. Add a `--format markdown` option to the `dataset-stats` command handler in `src/openbench/cli.py`.
  2. Format the output as a GitHub-flavored Markdown table, ensuring all values pass through `escape_markdown_cell` to properly sanitize pipes (`|`) and newlines (`\n`).
  3. Regenerate reference documentation via `python scripts/generate_reference_docs.py`.
  4. Add robust unit tests with `tmp_path` fixtures covering edge-case characters.

  Could you please assign this issue to me?
  ```