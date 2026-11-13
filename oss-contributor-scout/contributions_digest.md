# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-13)

---

### ### [Issue #1: Use Product Hunt's official API instead of scraping](https://github.com/Poushali-02/seedreach/issues/15) · 11 stars

- **Profile Value:** Demonstrates your ability to modernize brittle web scrapers into robust, production-grade applications using official GraphQL APIs and graceful fallback patterns.
- **The Challenge:** Replace the unreliable web scraping implementation in `src/sourcing/product_hunt.py` with Product Hunt's official GraphQL API, while keeping a fallback mechanism if credentials are missing or requests fail.
- **Technical Plan:**
  1. Add `PRODUCTHUNT_API_TOKEN` to `.env.example`.
  2. Rewrite `src/sourcing/product_hunt.py` to query the official GraphQL endpoint (`https://api.producthunt.com/v2/api/graphql`).
  3. Wrap the API execution in a `try/except` block and implement a graceful fallback to the legacy scraper or empty state if the token is missing/invalid.
  4. Update `README.md` with instructions on how to generate and configure a Product Hunt Developer Token.
  5. Add `tests/test_product_hunt.py` using `unittest.mock` or `responses` to test both the happy path and the fallback path.

- **Ready-to-Post Claim Comment:**
```markdown
Hi @Poushali-02! I'd love to tackle this issue. Replacing the web scraper with the official Product Hunt GraphQL API (complete with a graceful fallback for missing tokens) is a great way to make the tool much more robust. 

My planned approach:
1. Update `.env.example` with `PRODUCTHUNT_API_TOKEN`.
2. Implement the GraphQL client in `src/sourcing/product_hunt.py` with proper error handling and fallback logic.
3. Update documentation in `README.md`.
4. Add unit tests in `tests/test_product_hunt.py` covering both authenticated and fallback scenarios.

Please assign this to me when you have a moment, and I'll get a PR open soon!
```

---

### ### [Issue #2: Add a funding-news source (startups that just raised)](https://github.com/Poushali-02/seedreach/issues/14) · 11 stars

- **Profile Value:** Highlights strong backend data-processing skills, RSS parsing proficiency, and the ability to design clean custom extraction algorithms to isolate target startup domains.
- **The Challenge:** Build a brand new lead source provider (`src/sourcing/funding_news.py`) that parses RSS feeds from tech/startup news outlets and intelligently extracts the startup's actual landing page while filtering out social media and investor links.
- **Technical Plan:**
  1. Create `src/sourcing/funding_news.py` modeling the architectural pattern of `src/sourcing/launch_hn.py`.
  2. Use `feedparser` to ingest RSS articles from targeted funding-announcement feeds.
  3. Implement URL parsing and regex/BeautifulSoup extraction logic to pull outbound links while filtering out blacklisted domains (e.g., Twitter, LinkedIn, VC websites).
  4. Register and invoke the new source inside `src/pipeline.py`.
  5. Document the new funding-news source configuration in `README.md`.
  6. Add unit tests in `tests/test_funding_news.py` using local XML fixtures to verify reliable domain extraction.

- **Ready-to-Post Claim Comment:**
```markdown
Hi @Poushali-02! This sounds like a fantastic addition to Seedreach. I'd love to implement the funding-news lead source.

My planned approach:
1. Create `src/sourcing/funding_news.py` following the existing pattern in `launch_hn.py` using `feedparser`.
2. Write robust link extraction and filtering logic to isolate the startup's actual website while ignoring social and investor links.
3. Integrate the new source into `src/pipeline.py`.
4. Update `README.md` and add unit tests with mock RSS fixtures in `tests/test_funding_news.py`.

Could you please assign this issue to me? Thanks!
```

---

### ### [Issue #3: `sqlmesh plan --restate-model` requires model files to be present](https://github.com/SQLMesh/sqlmesh/issues/3260) · 3,350 stars

- **Profile Value:** Showcases advanced debugging and contribution capability within a massive, highly respected production-grade data framework (`sqlmesh`), adding serious weight to your data or backend engineering resume.
- **The Challenge:** Fix a CLI workflow bottleneck where `sqlmesh plan --restate-model` strictly requires local model definition files to exist on disk, even when users need to restate data for models whose files have been removed or refactored.
- **Technical Plan:**
  1. Locate the validation check in the `plan` command handler (`sqlmesh/cli/` or context validation methods) where `--restate-model` checks for local model file presence.
  2. Relax the strict filesystem check so that SQLMesh checks the existing snapshot state / metadata store for the target model if its local definition file is missing.
  3. Ensure a clear, descriptive error is raised only if the model exists neither locally nor in historical snapshots.
  4. Add a comprehensive regression test in `tests/core/test_plan.py` where a model definition file is absent but restatement planning succeeds via historical snapshots.

- **Ready-to-Post Claim Comment:**
```markdown
Hi maintainers! I would love to pick up this issue. Removing the strict local file requirement for `--restate-model` when historical snapshots exist will be a great quality-of-life improvement for the CLI.

My planned approach:
1. Trace the validation logic in the `plan` command and `Context.plan()` where model file existence is enforced.
2. Update the check to fall back to the metadata store/snapshots if the local file is absent, while preserving helpful error messages for truly unknown models.
3. Add an integration test in `tests/core/test_plan.py` verifying successful plan generation when the local model file has been removed.

Could you please assign this issue to me? I'm ready to get started.
```