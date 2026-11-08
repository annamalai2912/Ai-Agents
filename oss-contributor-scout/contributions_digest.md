# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-08)

---

### Chained `$(parent).$(child)` queries the whole document when the parent is re-rendered during the implicit wait
* **Repo & URL:** [webdriverio/webdriverio #16395](https://github.com/webdriverio/webdriverio/issues/16395) (~9,871 stars)
* **Profile Value:** Fixing a race condition in element scoping and implicit waits for an industry-standard browser automation framework demonstrates elite-level mastery of async JavaScript internals and complex DOM mutations.
* **The Challenge:** When a chained query like `$(parent).$(child)` runs during an implicit wait, a re-render of the parent detaches its reference. Instead of re-fetching the parent first, the framework falls back to querying the entire document, breaking scoping boundaries.
* **Technical Plan:**
  1. Trace `packages/webdriverio/src/element.ts` and selector execution paths to identify how element search context references are maintained.
  2. Wrap child query execution in a self-healing retry wrapper that checks if the parent element reference has gone stale.
  3. Ensure that if the parent is detached/re-rendered during the implicit wait window, the parent is re-queried before evaluating the child relative to it.
  4. Write an integration test reproducing the async `setInterval` DOM mutation MRE to verify scoping integrity under re-render conditions.

* **Ready-to-Post Claim Comment:**
```markdown
Hi maintainers! I’ve taken a close look at this issue and reproduced the race condition scenario described in your MRE. 

I'd love to tackle this by implementing a self-healing parent reference check inside the element query retry loop in `packages/webdriverio/src/element.ts`. This will ensure that if a parent element is detached or re-rendered during an implicit wait, the framework re-queries the parent context rather than falling back to document-level scoping.

Could you please assign this issue to me? I'm ready to open a PR with a fix and an accompanying integration test.
```

---

### Ctrl+F doesn't toggle full-screen mode while Caps Lock is on
* **Repo & URL:** [martinfrancois/question-driven-talk-assistant #1096](https://github.com/martinfrancois/question-driven-talk-assistant/issues/1096) (7 stars)
* **Profile Value:** Resolving frontend accessibility and keyboard-event handling edge cases showcases meticulous attention to detail in UX and robust TypeScript event handling.
* **The Challenge:** The app listens for `Ctrl+F` to toggle full-screen, but checking `event.key === 'f'` fails when Caps Lock is active because `event.key` outputs an uppercase `"F"`.
* **Technical Plan:**
  1. Locate the window-level `keydown` event listener handling hotkeys in `src/App.tsx`.
  2. Replace or supplement the brittle `event.key.toLowerCase() === 'f'` condition with layout- and capitalization-independent `event.code === 'KeyF'`.
  3. Add a unit test in `src/__tests__/App.spec.tsx` simulating a keyboard event with `ctrlKey: true`, `code: 'KeyF'`, and `key: 'F'` (Caps Lock state) to ensure regressions are prevented.

* **Ready-to-Post Claim Comment:**
```markdown
Hello! I would love to contribute a fix for this keyboard event bug. 

The issue is straightforward: `KeyboardEvent.key` evaluates to uppercase `"F"` when Caps Lock is enabled. By switching the hotkey evaluation logic from `e.key` to `e.code === 'KeyF'` in the global keydown listener, we can make the full-screen shortcut completely robust against Caps Lock and modifier states.

Please assign this to me, and I'll submit a PR along with a unit test covering the Caps Lock edge case!
```

---

### `404.html` at the site root
* **Repo & URL:** [arminazimi/slipway #1067](https://github.com/arminazimi/slipway/issues/1067) (1 star)
* **Profile Value:** Contributing to an agent-native static site generator engine demonstrates your ability to work within clean modular architectures, build contracts, and output pipelines.
* **The Challenge:** Slipway's build engine lacks an automatic output generator to emit a standard root-level `404.html` file required by static hosts for client-side routing and graceful error handling.
* **Technical Plan:**
  1. Create a new output generator module at `packages/engine/src/outputs/not-found.ts` that compiles a clean 404 page markup using site config properties (such as `baseUrl`).
  2. Integrate `generateNotFoundPage` into the core build compilation pipeline in `packages/engine/src/builder.ts` to output `404.html` directly to the build root directory.
  3. Add unit tests in `packages/engine/src/outputs/not-found.test.ts` to verify asset URL resolution and proper markup generation.

* **Ready-to-Post Claim Comment:**
```markdown
Hi @arminazimi! I'd love to pick this up as a quick win since it's marked `good first issue` and `size: XS`.

My plan is to implement `packages/engine/src/outputs/not-found.ts`, wire it directly into the core output builder in `packages/engine/src/builder.ts`, and add unit tests to ensure root-relative URLs and base paths render correctly.

Could you please assign this issue to me?
```