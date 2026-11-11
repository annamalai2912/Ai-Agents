# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-11)

---

### 1. [`memtomem/memtomem` — Issue #3242](https://github.com/memtomem/memtomem/issues/3242) (★ 23)
- **Profile Value:** Showcases meticulous Python testing practices and rigorous edge-case handling using `pytest` parameterization for CLI utility functions.
- **The Challenge:** The private helper function `_parse_duration` (used by `mm session start --auto-end-stale`) lacks direct, comprehensive unit test coverage for valid duration formats and invalid inputs that trigger `click.BadParameter`.
- **Technical Plan:**
  1. Inspect `memtomem/cli.py` to examine the exact implementation and regex/parsing logic of `_parse_duration`.
  2. Create a dedicated test file `tests/test_parse_duration.py` to isolate the test suite.
  3. Implement `@pytest.mark.parametrize` matrices covering valid time units (`s`, `m`, `h`, `d`) and invalid cases (`""`, `"abc"`, `"10x"`, `"-5m"`).
  4. Run `pytest tests/test_parse_duration.py -v` to verify 100% test pass rates and proper exception raising.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I would love to tackle this issue and add comprehensive unit test coverage for `_parse_duration`. 

  My planned approach is:
  1. Isolate the parsing logic in `memtomem/cli.py`.
  2. Create a dedicated test module (`tests/test_parse_duration.py`) utilizing `pytest.mark.parametrize`.
  3. Cover valid string formats (`s`, `m`, `h`, `d`) as well as edge cases and invalid inputs that correctly trigger `click.BadParameter`.
  4. Validate everything locally via pytest.

  Please let me know if this sounds good, and feel free to assign this issue to me!
  ```

---

### 2. [`reticlehq/reticle` — Issue #1707](https://github.com/reticlehq/reticle/issues/1707) (★ 1,265)
- **Profile Value:** Demonstrates full-stack CLI tooling and Developer Experience (DX) competence on a fast-growing, high-visibility repository (1.2k+ stars).
- **The Challenge:** The project initialization flow (`init`) does not recognize Expo projects, and Expo web's default development port (`8081`) is missing from the dev-server port scanner manifest.
- **Technical Plan:**
  1. Inspect `init/src/detect/detect.ts` to understand how framework detection rules are structured and add Expo detection (`package.json` / `app.json` checks).
  2. Inspect `init/src/detect/dev-server-ports.ts` and add port `8081` to the default port registry.
  3. Add unit test coverage in `init/src/detect/__tests__/detect.test.ts` mocking an Expo workspace.
  4. Execute the test suite via `npm test` to verify correctness.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hello! I'd like to contribute a fix for Expo detection and port scanning support.

  My planned approach:
  1. Update `init/src/detect/detect.ts` to properly recognize Expo project structures and configuration files.
  2. Add port `8081` to the scanner manifest in `init/src/detect/dev-server-ports.ts`.
  3. Write corresponding unit tests in `detect.test.ts` to prevent regressions.
  4. Run the test suite locally.

  Could you please assign this issue to me? Thanks!
  ```

---

### 3. [`vllm-project/vllm-ascend` — Issue #14150](https://github.com/vllm-project/vllm-ascend/issues/14150) (★ 3,072)
- **Profile Value:** Highlights advanced systems-level problem solving, concurrency auditing, and multi-threading safety in distributed AI inference infrastructure.
- **The Challenge:** Under concurrent multi-threaded execution (background KV cache transfer threads interacting with forward pass read/write paths), unprotected or improperly locked accesses to `_invalid_block_ids` can lead to race conditions and state corruption.
- **Technical Plan:**
  1. Audit all references to `_invalid_block_ids` across the codebase using `git grep`.
  2. Analyze lock acquisition scopes and identify unprotected read/write operations.
  3. Wrap unprotected operations inside thread-safe critical sections using the appropriate locking primitives (e.g., `with self.lock:`).
  4. Write a multi-threaded stress test in `tests/core/` to simulate concurrent reads/mutations and verify thread safety.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi team, I would like to take on this concurrency audit task for `_invalid_block_ids`.

  My planned approach:
  1. Grep and inspect all code paths reading or mutating `_invalid_block_ids`.
  2. Audit lock scopes to ensure all access points are properly guarded under critical sections.
  3. Implement thread-safe synchronization to prevent race conditions during concurrent KV cache transfers and execution reads.
  4. Add a multi-threaded unit test verifying thread safety under high concurrency.

  Please assign this to me if it's still available. Thank you!
  ```