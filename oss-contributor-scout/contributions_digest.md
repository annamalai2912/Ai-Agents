# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-08)

---

### ### [security(har-import): credential warning covers headers and query strings but not request bodies](https://github.com/kurok/pywrkr/issues/305) • ⭐ 5
- **Profile Value:** Fixing security sanitization gaps in asynchronous HTTP tooling proves your ability to secure data pipelines and protect user credentials across protocol boundaries.
- **The Challenge:** `pywrkr`'s HAR import feature warns users when sensitive keys (like passwords or tokens) appear in headers or query strings, but fails to inspect request bodies (`postData`), allowing login payloads to be written to disk unflagged.
- **Technical Plan:**
  1. Inspect `pywrkr/har_import.py` to locate the current credential-scanning logic for headers and query parameters.
  2. Extend the scanner to handle `entry['request']['postData']`, parsing JSON bodies, URL-encoded form data, and raw text.
  3. Wire detected sensitive keys/patterns into the existing warning mechanism.
  4. Add a unit test in `tests/test_har_import.py` verifying that passwords within JSON request bodies successfully trigger a security warning.
- **Ready-to-Post Claim Comment:**
```markdown
Hi @kurok! I'd love to tackle this security gap. 

**Proposed Approach:**
1. Locate the header/query credential scanning utility inside `pywrkr/har_import.py`.
2. Extend inspection to `entry['request']['postData']`, properly parsing JSON, form-urlencoded, and raw text payloads.
3. Hook detected sensitive fields into the existing warning output.
4. Add a comprehensive regression test in `tests/test_har_import.py` covering JSON body credential leaks.

Could you please assign this issue to me? I'm ready to open a PR.
```

---

### ### [[quality] Nightly mutation run aborts in Stryker's dry run: package.test.ts cannot find STATIC_JS_ROUTES in instrumented dist/ui.js](https://github.com/hivecommons/promptargs/issues/460) • ⭐ 3
- **Profile Value:** Resolving CI/CD pipeline failures caused by mutation testing instrumentation demonstrates advanced proficiency with enterprise-grade quality tooling and bundler internals.
- **The Challenge:** Stryker instruments code prior to compilation for mutation testing, injecting runtime wrappers that alter variable structures and break `src/package.test.ts` regex scans for `STATIC_JS_ROUTES` in `dist/ui.js`.
- **Technical Plan:**
  1. Inspect `src/package.test.ts` to examine how it scans `dist/ui.js` for `STATIC_JS_ROUTES`.
  2. Update the regex matcher or parsing logic to gracefully handle Stryker instrumentation markers (e.g., mutant activation wrappers).
  3. Alternatively, review `stryker.config.mjs` to ensure proper test environment isolation if needed.
  4. Verify the fix by running local unit tests and executing `npx stryker run --dryRun`.
- **Ready-to-Post Claim Comment:**
```markdown
Hi maintainers! I would like to fix this nightly mutation testing abort.

**Proposed Approach:**
1. Investigate the regex/parsing logic inside `src/package.test.ts` that scans `dist/ui.js`.
2. Update the matcher to be resilient against Stryker's code instrumentation tokens and wrappers.
3. Validate the fix by running local tests and executing a Stryker dry run to ensure clean execution.

Please assign this issue to me when you have a moment. Thanks!
```