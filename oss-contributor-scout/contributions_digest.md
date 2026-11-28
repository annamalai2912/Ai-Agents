# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-28)

---

### ### [aws/jsii-compiler #3012](https://github.com/aws/jsii-compiler/issues/3012) • 49 stars
- **Profile Value:** Contributing to official AWS infrastructure toolchains demonstrates mastery over complex TypeScript Abstract Syntax Tree (AST) manipulations and compiler internals.
- **The Challenge:** When running `--strip-deprecated`, the compiler throws an unhandled assertion error ("Expected a ClassDeclaration") when it encounters a TypeScript class that has been merged with an interface of the same name.
- **Technical Plan:**
  1. Inspect `src/transforms/deprecated-remover.ts` and locate base class helper utilities (`replaceBaseClass`, `removeBaseClass`).
  2. Access declaration arrays safely via `node.symbol.declarations` rather than assuming index `0` is a class.
  3. Introduce robust type guards using `ts.isClassDeclaration` to filter out non-class members in merged declarations.
  4. Add a regression test case featuring a class-interface merge and verify compilation succeeds.
- **Ready-to-Post Claim Comment:**
```markdown
Hi maintainers! I'd love to tackle this issue. 

The bug is caused by blindly assuming `node.symbol.declarations[0]` is a `ts.ClassDeclaration` during AST traversal in `src/transforms/deprecated-remover.ts` when a class-interface merge occurs. 

**Proposed Plan:**
1. Update declaration lookup to safely check the array of symbol declarations.
2. Implement proper type guards (`ts.isClassDeclaration`) to ensure we only target the actual class node.
3. Add a unit test covering class-interface merging with `--strip-deprecated`.

Could you please assign this issue to me? Thanks!
```

---

### ### [aws/jsii-compiler #3025](https://github.com/aws/jsii-compiler/issues/3025) • 49 stars
- **Profile Value:** Fixing CLI option parsing and build orchestration bugs in AWS tools proves your ability to navigate build systems and the TypeScript Compiler API deeply.
- **The Challenge:** User-supplied `tsconfig.json` files featuring `"incremental": true` without an explicit `"tsBuildInfoFile"` fail with error `TS5074` because `jsii` fails to pass configuration path context down to `ts.createIncrementalProgram`.
- **Technical Plan:**
  1. Open `src/compiler.ts` and inspect how options are compiled and passed inside `buildOnce`.
  2. Ensure `configFilePath` from the parsed config is preserved and passed into the compiler program creation options.
  3. Alternatively, implement a safe default fallback for `tsBuildInfoFile` if incremental compilation is enabled.
  4. Write an integration test using a temporary custom `tsconfig.json` to verify the build runs cleanly without throwing TS5074.
- **Ready-to-Post Claim Comment:**
```markdown
Hello! I would like to pick up this issue. 

**Proposed Approach:**
I will inspect `src/compiler.ts` (`buildOnce`) to ensure that `configFilePath` from the parsed user config is correctly retained when invoking `ts.createIncrementalProgram`, allowing TypeScript to properly resolve paths and write the build info file. I'll also add an integration test to prevent future regressions.

Please assign this to me when you have a moment. Thank you!
```

---

### ### [CrossGL/crosstl #4639](https://github.com/CrossGL/crosstl/issues/4639) • 2,602 stars
- **Profile Value:** Contributing to a multi-language shading translation layer with over 2.6k stars showcases advanced competency in compiler backends, IR generation, and modern memory ownership models like Mojo.
- **The Challenge:** `mojo_codegen.py` incorrectly translates `out` and `inout` shader parameters as `owned` instead of mutable references (`mut`), preventing function writes from propagating back to callers.
- **Technical Plan:**
  1. Navigate to `crosstl/codegen/mojo_codegen.py` and locate function signature and parameter formatting logic.
  2. Review parameter qualifier mappings and update `out`/`inout` translation to emit `mut` references instead of `owned`.
  3. Verify that call sites and argument passing rules align with Mojo's borrowing and reference specifications.
  4. Add a test case with an `inout` parameter compute shader and run pytest to confirm correct Mojo code output and prevent regressions.
- **Ready-to-Post Claim Comment:**
```markdown
Hi team! I'd love to contribute a fix for this Mojo codegen bug.

**Proposed Solution:**
I will update `crosstl/codegen/mojo_codegen.py` to map `out` and `inout` shader qualifiers to Mojo's mutable reference keyword (`mut`) rather than `owned`, ensuring writes correctly propagate to callers. I'll also add a test case to validate the generated Mojo output.

Could you please assign this issue to me? Thanks!
```