# 🧠 Daily AI Research Digest (2026-11-25)

---

### [SAG-Mem-1.0 Technical Report](https://arxiv.org/abs/2611.33124v1)
* **Authors:** SAG-Mem Research Team
* **The 30-Second Summary:** Traditional conversational memory relies on expensive LLM summarization loops and heavy vector-embedding pipelines that introduce high latency and drop verbatim details. SAG-Mem solves this by utilizing a zero-inference write-time architecture paired with a multi-round BM25 lexical expansion and lightweight evidence evaluation at query time.
* **The Breakthrough Explained:** 
  Instead of using an LLM to extract or summarize text, SAG-Mem stores complete dialogue messages in clean, non-overlapping chunks with *zero model inference required during write-time*. At query time, it uses smart multi-round lexical expansion via BM25 paired with a lightweight evidence evaluator. It proves you don't need heavy semantic embedding extraction for long-term memory—just clean chunking and intelligent lexical routing, which drastically drops storage and indexing costs while outperforming complex memory architectures on benchmarks like LoCoMo and LongMemEval.
* **🛠️ How You Can Apply This (Developer Takeaway):** 
  Replace your heavy vector-embedding generation pipeline and background LLM summarization workers with a hybrid BM25 + chunked raw-text store. 
  ```python
  from rank_bm25 import BM25Okapi

  class ZeroInferenceMemory:
      def __init__(self):
          self.chunks = []
          self.tokenized_corpus = []

      def add_turn(self, speaker: str, message: str):
          # Zero-inference write: store raw text chunk and tokenize for BM25
          chunk = f"{speaker}: {message}"
          self.chunks.append(chunk)
          self.tokenized_corpus.append(chunk.lower().split())

      def query_memory(self, query: str, top_k: int = 3) -> list[str]:
          # Query-time lexical routing via BM25
          bm25 = BM25Okapi(self.tokenized_corpus)
          tokenized_query = query.lower().split()
          scores = bm25.get_scores(tokenized_query)
          
          # Return top scoring raw chunks instantly without embedding lookups
          top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
          return [self.chunks[i] for i in top_indices]
  ```
* **PDF Link:** [https://arxiv.org/pdf/2611.33124v1.pdf](https://arxiv.org/pdf/2611.33124v1.pdf)

---

### [CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies](https://arxiv.org/abs/2611.33148v1)
* **Authors:** CoT-Proxy Research Contributors
* **The 30-Second Summary:** Distilling expensive frontier reasoning models (which output hidden chains-of-thought) into fast local models is difficult because teachers hide internal traces and lengthy reasoning introduces massive latency. CoT-Proxy bypasses this by training student models purely on final actions using lightweight "CoT-proxies" and a KL divergence penalty, allowing local models to activate their own native thinking style at inference time.
* **The Breakthrough Explained:** 
  CoT-Proxy demonstrates a counterintuitive breakthrough: **you can completely drop the hidden chain-of-thought during fine-tuning.** By training a smaller student model purely on the teacher's final actions (combined with a KL divergence penalty to prevent drift) and using short post-action reasoning summaries ("CoT-proxies"), the student learns to behave like the frontier teacher. Crucially, at inference time, the student can *enable its own thinking style* and achieve massive accuracy boosts (e.g., jumping from 7% to 48% on AppWorld using GPT-derived trajectories), giving teams a direct recipe to distill closed models into fast local actors.
* **🛠️ How You Can Apply This (Developer Takeaway):** 
  When building a dataset to distill a proprietary reasoning model (like OpenAI o1/o3 or DeepSeek-R1) into an open-weights model (like Qwen-7B), strip out the verbose hidden thought tokens. Train only on the final tool calls/actions, accompanied by a compressed 1-sentence post-action justification schema:
  ```json
  {
    "context": "User requested database migration script.",
    "action_proxy": "Used python script to parse schema because direct SQL dump failed.",
    "final_action": "EXECUTE python parse_schema.py"
  }
  ```
* **PDF Link:** [https://arxiv.org/pdf/2611.33148v1.pdf](https://arxiv.org/pdf/2611.33148v1.pdf)

---

### [BriConstrain: Geometrically Constrained Decoding for Autoregressive Brick Assembly Generation](https://arxiv.org/abs/2611.33135v1)
* **Authors:** BriConstrain Lab
* **The 30-Second Summary:** Autoregressive models generating structured, physical, or multi-step configurations often hallucinate invalid states, forcing engineers to rely on wasteful "rejection sampling" loops. BriConstrain introduces geometrically constrained decoding, which intercepts next-token probabilities live at inference time to mask out invalid options using a structural oracle.
* **The Breakthrough Explained:** 
  Instead of letting a model generate blindly and discarding bad outputs, BriConstrain intercepts the model's next-token probabilities *live at inference time* and dynamically masks out invalid options using a structural/geometric oracle. It guarantees 100% validity on-the-fly without needing expensive, retry-heavy agentic loops, completely eliminating invalid generation states in spatial and structural assembly tasks.
* **🛠️ How YouCan Apply This (Developer Takeaway):** 
  Implement a custom Logits Processor in your generation loop (e.g., using Hugging Face Transformers) to prune syntax, structural, or business logic violations token-by-token:
  ```python
  import torch
  from transformers import LogitsProcessor

  class StructuralConstraintLogitsProcessor(LogitsProcessor):
      def __init__(self, invalid_token_ids_fn):
          self.invalid_token_ids_fn = invalid_token_ids_fn

      def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:
          # Compute invalid tokens dynamically based on current generation state (the structural oracle)
          invalid_ids = self.invalid_token_ids_fn(input_ids)
          for token_id in invalid_ids:
              scores[:, token_id] = -float('inf')  # Mask out invalid choices entirely
          return scores
  ```
* **PDF Link:** [https://arxiv.org/pdf/2611.33135v1.pdf](https://arxiv.org/pdf/2611.33135v1.pdf)

---

### 💡 Builder Trend of the Day
The common thread binding these three papers is a decisive industry shift away from **costly runtime inference loops and brute-force trial-and-error** (like LLM summarizers, heavy embedding searches, retry-heavy agent loops, and rejection sampling). Instead, AI architecture is moving toward **deterministic structural engineering**: zero-inference lexical chunking for memory, decoupled post-action distillation for reasoning, and live logits-level masking for generation constraints. For builders, the message is clear: make your infrastructure deterministic, structural, and lightweight, letting the model focus purely on core value generation rather than computational housekeeping.