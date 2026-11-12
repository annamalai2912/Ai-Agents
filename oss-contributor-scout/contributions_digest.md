# 🚀 Open-Source Contribution Opportunities (Generated 2026-11-12)

- ### 1. [Add RAGAS evaluation benchmark suite (faithfulness & answer relevancy)](https://github.com/Data-science-and-analytics-by-shivansh/Enterprise-Knowledge-Agent-RAG-/issues/2) *(Stars: 0)*
- **Profile Value:** Demonstrates advanced AI engineering skills in LLM application evaluation, metric design, and CI quality gating using RAGAS.
- **The Challenge:** The repository lacks automated evaluation metrics to measure output quality, making it difficult to detect regressions in prompt design, chunking, or retrieval strategies.
- **Technical Plan:**
  1. Add `ragas` and `datasets` to `requirements.txt`.
  2. Create a golden evaluation dataset (`evaluation/test_dataset.json`) with sample questions, contexts, answers, and ground truths.
  3. Implement the evaluation harness (`evaluation/evaluate_rag.py`) leveraging LangChain and RAGAS metrics (*faithfulness*, *answer_relevancy*, *context_precision*).
  4. Wrap the evaluation runner inside an automated pytest suite (`tests/test_evaluation.py`) enforcing minimum score thresholds.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi @Data-science-and-analytics-by-shivansh, I would love to tackle this issue and add a robust RAGAS evaluation framework! 

  My plan is to:
  1. Add `ragas` and `datasets` to `requirements.txt`.
  2. Create a domain-specific golden evaluation dataset under `evaluation/test_dataset.json`.
  3. Implement the evaluation harness script (`evaluation/evaluate_rag.py`) to measure *faithfulness*, *answer_relevancy*, and *context_precision*.
  4. Integrate a pytest wrapper (`tests/test_evaluation.py`) to enforce quality thresholds in CI.

  Could you please assign this issue to me? I'll have a clean PR ready shortly!
  ```

---

- ### 2. [Checks: use assert instead of returning True](https://github.com/amirouche/bb.py/issues/86) *(Stars: 6)*
- **Profile Value:** Showcases strong command over Python idioms, refactoring discipline, error-handling patterns, and test-driven development (TDD).
- **The Challenge:** Existing check and validation utilities return boolean values (`True`/`False`) instead of raising native `AssertionError` exceptions, requiring a comprehensive codebase refactor of checks, error-explanation wrappers, tests, and documentation.
- **Technical Plan:**
  1. Audit and locate all functions returning boolean check statuses.
  2. Refactor functions to use native `assert` statements with descriptive failure messages.
  3. Update error explanation/interception logic (e.g., `check_explain`) to catch `AssertionError` instead of checking for falsy return values.
  4. Update the test suite to use `pytest.raises(AssertionError)` and check documentation/transcripts for outdated examples.
- **Ready-to-Post Claim Comment:**
  ```markdown
  Hi @amirouche, I'd like to help refactor the checking framework to use native `assert` statements instead of returning boolean values.

  My planned approach:
  1. Identify and refactor check functions across the library to raise `AssertionError` with descriptive failure messages.
  2. Update error-explanation wrappers (like `check_explain`) to catch `AssertionError` and format failure reports.
  3. Update `tests/` to use `pytest.raises(AssertionError)`.
  4. Review and update documentation/transcripts to align with the new assertion-based paradigm.

  Please assign this issue to me when you get a chance!
  ```