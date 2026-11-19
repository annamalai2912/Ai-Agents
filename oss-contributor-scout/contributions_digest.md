# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-19)

- ### [CLI] Evidence & Provenance Artifact Exporter (JSONL & Markdown Incident Brief) [Level 1](https://github.com/Shinraya-Tech-Labs/AgentWatch/issues/739) — Repo Stars: 33
- **Profile Value:** Mastering AI agent observability and structured CLI data exports highlights your ability to design clean, production-ready developer tooling for cutting-edge LLM ecosystems.
- **The Challenge:** Implement an `agentwatch export` sub-command to package audit logs, evidence, and provenance traces into stream-oriented JSONL and human-readable Markdown incident briefs without heavy external dependencies.
- **Technical Plan:**
  1. Create `agentwatch/exporters/artifact_exporter.py` containing serialization logic for JSONL line-by-line dumps and structured Markdown generation.
  2. Implement the `export` sub-command in `agentwatch/cli/v3.py` supporting `--input`, `--format [jsonl|markdown]`, and `--output` options using standard library modules only.
  3. Write comprehensive unit tests in `tests/cli/test_export.py` covering file generation, format validity, and CLI execution via Click's `CliRunner`.
  4. Run quality checks (`ruff`, `pytest`, `bandit`) to ensure robust code standards.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to pick up this issue. 

  My planned approach is to build a lightweight exporter service in `agentwatch/exporters/artifact_exporter.py` utilizing Python's standard library (`json`, `pathlib`) to avoid heavy external dependencies. I'll wire up the `export` sub-command in `agentwatch/cli/v3.py` for both `jsonl` and `markdown` formats, and add complete unit tests in `tests/cli/test_export.py` verified via `pytest` and `ruff`.

  Please assign this to me when you have a moment!
  ```

---

- ### [Say the allowed variant, met and model names in words, not as a regex](https://github.com/jmineau/runtraj/issues/25) — Repo Stars: 0
- **Profile Value:** Improving developer experience (DX) through intuitive configuration error messages demonstrates strong user-centric design thinking and attention to API polish.
- **The Challenge:** Translate cryptic Pydantic regular expression validation errors (e.g., `must match ^[a-z0-9][a-z0-9-]*$`) into readable, natural language descriptions for configuration variants, meteorological datasets, and model names.
- **Technical Plan:**
  1. Inspect `runtraj/config.py` to identify field validators and regex constraint definitions for variant, met, and model parameters.
  2. Refactor validation error handling (using custom Pydantic validators or exception wrappers) to replace raw regex strings with descriptive plain-English rules.
  3. Add unit test assertions in `tests/test_config.py` verifying that invalid inputs raise user-friendly error messages entirely free of regex syntax.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hello! I would love to tackle this UX improvement. 

  I plan to update the validation constraints in `runtraj/config.py` to intercept regex mismatch errors and replace them with clear, human-readable natural language instructions. I will also add comprehensive tests in `tests/test_config.py` to ensure the new error messages are accurate and user-friendly.

  Could you please assign this issue to me?
  ```

---

- ### [Docs: a page for people asking 'my transfer is stuck, did I lose money?'](https://github.com/xebra-org/xebra/issues/128) — Repo Stars: 2
- **Profile Value:** Writing empathetic, clear technical documentation for decentralized cross-chain protocols showcases your capability to communicate complex system behaviors and mitigate user friction.
- **The Challenge:** Create a dedicated MDX guide addressing user anxiety over "stuck" Circle CCTP USDC transfers across L1s/L2s, detailing common causes, step-by-step on-chain verification, and support channels.
- **Technical Plan:**
  1. Draft the guide at `apps/docs/content/docs/guides/my-transfer-is-stuck.mdx` with proper frontmatter and structured sections covering reassurance, common bottlenecks, and block explorer verification.
  2. Update documentation navigation or sidebar configuration if required.
  3. Run local workspace validation using `pnpm --filter docs build` and `pnpm --filter docs check:links` to guarantee zero broken links and a clean build.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi team! I'd like to write this guide to help ease user anxiety around cross-chain transfer delays.

  I'll add the new MDX file at `apps/docs/content/docs/guides/my-transfer-is-stuck.mdx` covering CCTP reassurance, common delay causes, and explorer verification steps, then validate everything locally using `pnpm --filter docs build` and `pnpm --filter docs check:links`.

  I'd appreciate it if you could assign this to me!
  ```