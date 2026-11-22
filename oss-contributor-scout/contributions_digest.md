# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-22)

---

### 1. [cubrid-lab/cubrid-cookbook-python #580](https://github.com/cubrid-lab/cubrid-cookbook-python/issues/580) — *bug: preserve CSV export failures when pandas recipe cleanup fails*
- **Repo Star Count:** 28 stars
- **Profile Value:** Demonstrates mastery over robust systems engineering, resource management, and clean error propagation in Python data pipelines.
- **The Challenge:** A data export recipe cleans up temporary resources in a `finally` block, but if the primary CSV export fails, the cleanup exception overrides and swallows the original error, masking the root cause.
- **Technical Plan:**
  1. Locate the pandas CSV export recipes and underlying database session/temporary file teardown logic.
  2. Implement a protected try-except-finally block that preserves the primary exception (using exception chaining or local capture) while still executing cleanup.
  3. Ensure cleanup failures during an active primary error are safely logged rather than raised.
  4. Write a robust pytest regression test mocking both export and cleanup failures to verify original error preservation.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to tackle this issue. Swallowed root-cause exceptions during resource teardown can make debugging data pipelines painful. 

  My plan is to update the recipe execution wrapper to capture and preserve the primary CSV export exception while ensuring `finally` cleanup routines execute safely. I'll also add a dedicated regression test with pytest covering this exact error scenario. Could you please assign this issue to me? Thanks!
  ```

---

### 2. [teamrig/teamrig #834](https://github.com/teamrig/teamrig/issues/834) — *`meeting schedule --meets team/id` is refused for a sub-team's session*
- **Repo Star Count:** 2 stars
- **Profile Value:** Showcases practical TypeScript development and CLI design skills within the emerging AI agent-orchestration ecosystem.
- **The Challenge:** The CLI tool fails to recognize or validate hierarchical sub-team identifiers (e.g., `parent-team/sub-team`) when running meeting scheduling commands due to flat string lookup restrictions.
- **Technical Plan:**
  1. Inspect `src/cli/commands/meeting.ts` and core team resolution/validation helpers.
  2. Refactor the team identifier validation logic to support hierarchical path traversal instead of a flat lookup.
  3. Ensure uniform support across both `meeting schedule` and `meeting start` sub-commands.
  4. Add Jest integration/unit test cases verifying successful scheduling for valid sub-teams and clean error handling for invalid paths.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hello! I'd like to work on fixing this. It looks like the team lookup logic needs to support hierarchical path parsing for sub-teams when handling `--meets`. 

  My approach is to update the team resolution helper used by meeting commands to recursively traverse team hierarchies and add comprehensive Jest test cases for sub-team meeting scheduling. Please assign this to me when you have a moment!
  ```

---

### 3. [cubrid-lab/cubrid-cookbook-python #581](https://github.com/cubrid-lab/cubrid-cookbook-python/issues/581) — *bug: honor environment markers in cookbook dependency preflight*
- **Repo Star Count:** 28 stars
- **Profile Value:** Highlights deep familiarity with Python packaging ecosystems, PEP 508 environment markers, and preflight validation standards.
- **The Challenge:** Static dependency preflight checks fail or warn incorrectly on modern Python versions because they do not evaluate PEP 508 environment markers (e.g., `python_version<'3.12'`).
- **Technical Plan:**
  1. Locate the dependency preflight checker under `src/cubrid_cookbook/preflight/`.
  2. Integrate `packaging.requirements.Requirement` and evaluate `req.marker` dynamically against the running runtime environment.
  3. Filter out non-applicable conditional requirements before performing version checks.
  4. Add pytest fixtures and unit tests covering environment-dependent markers across different Python interpreter versions.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'm interested in solving this packaging preflight issue. 

  My plan is to integrate `packaging.requirements` and evaluate PEP 508 environment markers dynamically during preflight checks so conditional dependencies are correctly handled based on the runtime environment. I'll also add unit tests with environment-dependent fixtures. Could you assign this issue to me? Thank you!
  ```