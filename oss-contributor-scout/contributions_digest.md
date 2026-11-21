# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-21)

---

### 1. [Daily-spending check undercounts when an agent has more than 200 activities](https://github.com/naninu123/4evergent/issues/260) (⭐ 5)
* **Profile Value:** Fixing authorization/spending logic vulnerabilities in financial and AI agent infrastructure demonstrates high-stakes backend state validation mastery for your portfolio.
* **The Challenge:** The policy engine uses a hardcoded limit (`listByAgent(agentId, 200)`) to check daily spending. If an agent executes over 200 activities in a day, transactions past the 200-item window are silently truncated, allowing agents to bypass spending limits.
* **Technical Plan:**
  1. Inspect `src/store/ActivityStore.ts` and `src/policy/PolicyEngine.ts`.
  2. Extend `ActivityStore` to support a time-bounded query (e.g., `sumCostsByAgentSince(agentId, startOfDay)`) or implement an iterative pagination loop in `PolicyEngine.getDailySpent`.
  3. Update `PolicyEngine.getDailySpent` to calculate the accurate cumulative sum using the UTC day start timestamp.
  4. Add unit tests covering datasets exceeding 200 daily activities and edge cases around day boundaries.
* **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I’d love to tackle this issue. 

  **Planned Approach:**
  I will update `PolicyEngine.getDailySpent` and the `ActivityStore` layer to avoid arbitrary pagination truncation. Instead of fetching a hardcoded limit of 200 records, I will implement a time-bounded query/pagination mechanism filtering from the start of the current UTC day to ensure all daily activities are accurately summed. I'll also add comprehensive unit tests covering over-limit datasets and day-boundary edge cases.

  Please assign this to me when you have a moment!
  ```

---

### 2. [Add unit tests for the simulator process reader and stderr tail buffer](https://github.com/blockchain-maxis/signet/issues/924) (⭐ 3)
* **Profile Value:** Showcases advanced Go systems-programming competence, rigorous edge-case testing, and deep familiarity with low-level process management and buffer handling.
* **The Challenge:** The signet CLI simulator manages background processes and streams but lacks exhaustive table-driven unit test coverage in Go (`cli/internal/simulator/process_test.go`) for line framing, CRLF handling, and buffer limits.
* **Technical Plan:**
  1. Inspect `cli/internal/simulator/process.go` to understand `readLine`, `tailBuffer`, and stream reader signatures.
  2. Create/expand `cli/internal/simulator/process_test.go`.
  3. Implement table-driven tests for line framing/CRLF normalization, tail-buffer capacity constraints (64 KiB/64 MiB limits dropping old entries correctly), and unterminated streams.
  4. Run `go test -v -race` to verify concurrency safety and correctness.
* **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I would like to pick this up and add the requested unit tests.

  **Planned Approach:**
  I'll write comprehensive table-driven tests in `cli/internal/simulator/process_test.go` covering:
  1. Line framing and mixed CRLF (`\n` vs `\r\n`) normalization.
  2. Tail-buffer capacity limits and ring-buffer drop behavior under overflow.
  3. Unterminated stream handling (EOF mid-line).

  I'll ensure all tests pass cleanly under the Go race detector. Please assign this issue to me!
  ```

---

### 3. [Add `contracts update <id>`](https://github.com/cyfer-codes/stellarlens/issues/123) (⭐ 3)
* **Profile Value:** Demonstrates end-to-end command-line interface design, SDK integration, and robust developer ergonomics/error management for a specialized Web3 indexing platform.
* **The Challenge:** Stellarlens lacks a CLI command to update tracked Soroban smart contract metadata (like display names via `--name`), requiring manual database intervention or re-adding contracts.
* **Technical Plan:**
  1. Locate command definitions and service layers (e.g., `cmd/` and `internal/services/contracts.go`).
  2. Implement the new `contracts update <id>` subcommand with the optional `--name` flag.
  3. Add input validation ensuring `--name` is provided and non-empty, returning a clean usage error if omitted.
  4. Wire up the SDK/service layer to safely update the database record and handle non-existent contract IDs gracefully.
  5. Add CLI integration tests and verify manually.
* **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to contribute and implement the `contracts update <id>` command.

  **Planned Approach:**
  1. Register the new `update` subcommand under the contracts CLI command with positional `<id>` argument and `--name` flag.
  2. Implement validation to ensure `--name` is provided and non-empty, returning clear usage errors otherwise.
  3. Wire up the service/SDK layer to handle database updates securely with proper "contract not found" handling.
  4. Add CLI unit and integration tests.

  Could you please assign this issue to me?
  ```