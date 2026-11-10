# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-10)

---

### Issue 1: Add GET /admins for the indexed contract admin set
* **Repo & Issue:** [D-Indexer/Indexer-Backend #138](https://github.com/D-Indexer/Indexer-Backend/issues/138) ⭐ 9 stars
* **Profile Value:** Demonstrates production-grade Web3 backend architecture mastery, clean separation of concerns (services, controllers, routes), and rigorous PostgreSQL query design.
* **The Challenge:** Expose a new REST endpoint (`GET /admins`) to query the indexed contract administrator set, complete with Zod validation, camelCase mapping, and database query optimization.
* **Technical Plan:**
  1. Inspect existing service (`src/services/portfolio.ts`) and controller patterns.
  2. Implement `src/services/admins.ts` with explicit column selection (no `SELECT *`) and snake_case to camelCase field mapping.
  3. Implement `src/controllers/admins.ts` to handle request execution, errors, and `200 OK` responses.
  4. Wire up the Express router in `src/routes/admins.ts` and mount it under `/admins`.
  5. Add Zod schema validation for any query parameters.
  6. Write integration tests using `supertest` in `tests/admins.test.ts`.
* **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to take on this issue. 

  My planned approach:
  1. Create a dedicated service (`src/services/admins.ts`) executing an optimized query (explicit column selection, avoiding `SELECT *`) with snake_case-to-camelCase mapping.
  2. Implement the corresponding controller (`src/controllers/admins.ts`) and register a new Express route (`GET /admins`).
  3. Add robust Zod validation for query parameters and handle errors gracefully.
  4. Write comprehensive integration tests in `tests/admins.test.ts` verifying correct JSON payloads and status codes.

  Please assign this to me, and I'll have a clean PR ready shortly!
  ```

---

### Issue 2: Paginate GET /templates with a keyset cursor
* **Repo & Issue:** [D-Indexer/Indexer-Backend #137](https://github.com/D-Indexer/Indexer-Backend/issues/137) ⭐ 9 stars
* **Profile Value:** Showcases senior-level backend engineering skills by replacing naive `OFFSET` pagination with scalable keyset (cursor-based) pagination.
* **The Challenge:** Refactor the `GET /templates` endpoint to use keyset pagination (`WHERE id > $1 ORDER BY id LIMIT $2`), validate inputs with Zod, handle `400 Bad Request` edge cases, and return `nextAfter` metadata.
* **Technical Plan:**
  1. Define strict Zod validation schemas for query parameters (`limit` and `cursor`), returning `400` on failure.
  2. Update `src/services/templates.ts` to implement cursor-based parameterized SQL filtering.
  3. Calculate and attach the `nextAfter` cursor in the pagination response metadata.
  4. Write automated test suites in `tests/templates.test.ts` covering initial fetches, subsequent batched pagination, and invalid cursor error handling.
* **Ready-to-Post Claim Comment:**
  ```markdown
  Hello! I would love to contribute by implementing keyset pagination for `GET /templates`.

  My planned approach:
  1. Update query parameter validation using Zod to strictly validate `limit` and `cursor` inputs, returning `400 Bad Request` on malformed values.
  2. Refactor `src/services/templates.ts` to use a cursor-based SQL pattern (`WHERE id > $1 ORDER BY id LIMIT $2`) for optimal performance at scale.
  3. Calculate the `nextAfter` cursor and format the response payload to include clean pagination metadata.
  4. Add unit and integration test coverage in `tests/templates.test.ts` for boundary conditions and sequential batching.

  Could you please assign this issue to me? Thanks!
  ```

---

### Issue 3: Add an --output option for the Chrome CSV path
* **Repo & Issue:** [MehdiMamas/bitwarden-to-apple-keychain-converter-script #5](https://github.com/MehdiMamas/bitwarden-to-apple-keychain-converter-script/issues/5) ⭐ 1 star
* **Profile Value:** Highlights strong developer experience (DX) focus, clean Python CLI script design using `argparse`, and rigorous test-driven documentation updates.
* **The Challenge:** Add an optional `--output` / `-o` flag to the CLI utility to allow users to specify a custom destination path for the converted CSV file while preserving backward-compatible defaults.
* **Technical Plan:**
  1. Update `argparse` configuration in the primary Python script to accept `-o` / `--output` with a sensible default value.
  2. Refactor core file I/O functions to accept the dynamic output path variable.
  3. Update `README.md` usage documentation with clear examples of the new flag.
  4. Write pytest tests verifying file creation at custom paths via `tmp_path` fixtures alongside fallback default behavior.
* **Ready-to-Post Claim Comment:**
  ```markdown
  Hi! I'd like to pick up this task and add the `--output` CLI option.

  My planned approach:
  1. Update `argparse` in the main script to introduce an optional `-o / --output` argument while keeping the existing default output filename intact.
  2. Pass the custom output path dynamically into the conversion logic.
  3. Update the `README.md` to document the new flag with usage examples.
  4. Add a pytest test case using temporary directories to ensure custom output paths and fallback defaults work reliably.

  Please assign this issue to me!
  ```