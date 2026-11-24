# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-24)

---

### 1. [Add Retry-After on 429 responses consistently](https://github.com/TevaLabs/Xelma-Backend/issues/1057) (⭐ 6)
- **Profile Value:** Demonstrates mastery over robust API design, HTTP specifications (RFC 6585), and backend middleware implementation.
- **The Challenge:** The API currently returns an HTTP `429 Too Many Requests` status code when rate limits are exceeded, but omits the required `Retry-After` header.
- **Technical Plan:**
  1. Inspect `src/middleware/rateLimiter.middleware.ts` to locate where rate limits are enforced.
  2. Calculate the delta in seconds between the current timestamp and the rate-limit reset timestamp.
  3. Set the `Retry-After` header explicitly on the response object before returning `429`.
  4. Write a Jest test case to verify the presence and validity of the `Retry-After` header under rate-limited conditions.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi maintainers! I'd love to pick up this issue. I plan to update `src/middleware/rateLimiter.middleware.ts` to calculate the reset delta and inject the standard `Retry-After` header on all 429 responses, accompanied by a Jest test to prevent regressions. Please assign this to me when you have a moment!
  ```

---

### 2. [Smoke test covers hackathon health path](https://github.com/TevaLabs/Xelma-Backend/issues/1052) (⭐ 6)
- **Profile Value:** Highlights strong DevOps, CI/CD pipeline reliability, and test automation practices.
- **The Challenge:** The smoke test suite (`scripts/smoke-test.js`) uses a hardcoded health-check endpoint rather than respecting custom paths defined via the `HEALTHCHECK_PATH` environment variable.
- **Technical Plan:**
  1. Open `scripts/smoke-test.js` and analyze the target URL generation logic.
  2. Update the script to read `process.env.HEALTHCHECK_PATH` with a fallback default of `/health`.
  3. Ensure the dynamically constructed URL is logged cleanly for CI debugging purposes.
  4. Perform a local dry-run verification using custom environment variables.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hello! I can take care of this smoke test fix. I'll update `scripts/smoke-test.js` to dynamically pick up `HEALTHCHECK_PATH` with a robust fallback so custom deployment environments are validated correctly. Please assign this to me!
  ```

---

### 3. [Run the native wave64 BVH fixture on a supported Windows GPU](https://github.com/R0Y00/Xbox2Windows/issues/1) (⭐ 1,758)
- **Profile Value:** Showcases advanced low-level systems research, DirectX 12 graphics pipeline debugging, and hardware compatibility testing in a high-visibility repository.
- **The Challenge:** Empirical validation of compiled wave64 Bounding Volume Hierarchy (BVH) raytracing/compute fixtures is required on a compatible Windows GPU using the repo's PowerShell check scripts.
- **Technical Plan:**
  1. Set up a Windows machine with a modern discrete GPU supporting hardware raytracing and wave64 execution.
  2. Run the repository's capability detection PowerShell script (`tools/check-gpu-caps.ps1`) to verify driver and DX12 support.
  3. Execute the native wave64 BVH shader workload and capture performance/correctness metrics.
  4. Format the hardware diagnostic report and submit a documentation/coverage table update via PR.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi! I have a compatible Windows GPU setup ready and would love to run the native wave64 BVH fixture. I can execute the capability checks, record the benchmark/correctness metrics, and submit the coverage report update. Could you assign this issue to me?
  ```