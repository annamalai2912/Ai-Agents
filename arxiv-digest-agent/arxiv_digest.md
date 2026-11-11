# 🧠 Daily AI Research Digest (2026-11-11)

---

### [ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows](https://arxiv.org/abs/2611.14492v1)
* **Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama
* **The 30-Second Summary:** Building dynamic agent workflows with LLMs is easy for prototyping, but production deployment fails due to high latency, unpredictable non-determinism, and exorbitant token costs. *ReTrace* solves this by mining successful agent execution logs, extracting their underlying routing logic, and compiling them into deterministic, planner-free Python code.
* **The Breakthrough Explained:** Instead of relying on an expensive LLM to make decisions at every single step of a multi-step task, *ReTrace* replaces the runtime agent loop with compiled conditional routing rules. By converting dynamic prompt-and-response orchestration into a standard programmatic script, execution bypasses redundant LLM inference calls entirely while preserving the exact pathing needed to complete complex tool-use sequences.
* **🛠️ How You Can Apply This (Developer Takeaway):** Transition fragile agent loops to deterministic state machines once you have gathered enough successful trace telemetry. Here is a conceptual Python pattern showing how to replace a dynamic LLM router with a static compiled decision function:

```python
from typing import Dict, Any, Callable
import json

# BEFORE: Dynamic LLM Agent Loop (High latency, expensive tokens)
def run_dynamic_agent_step(state: Dict[str, Any]) -> str:
    prompt = f"Given state {state}, should we call 'sql_tool' or 'api_tool' or 'finish'?"
    # response = expensive_llm.generate(prompt)
    return "sql_tool" # simulated LLM decision

# AFTER (ReTrace Pattern): Compiled Deterministic State Machine
class CompiledWorkflow:
    def __init__(self):
        # Compiled routing rules mined from successful agent logs
        self.transition_rules: Dict[str, Callable[[Dict[str, Any]], str]] = {
            "start": lambda s: "sql_tool" if "database" in s.get("query", "").lower() else "api_tool",
            "sql_tool": lambda s: "finish" if s.get("sql_results") else "sql_tool"
        }

    def execute(self, initial_state: Dict[str, Any]) -> Dict[str, Any]:
        state = initial_state
        step = "start"
        while step != "finish":
            next_step_func = self.transition_rules.get(step)
            if not next_step_func:
                raise ValueError(f"No compiled path for step: {step}")
            step = next_step_func(state)
            # Execute deterministic action instead of LLM planning
            state["last_executed"] = step
        return state

# Drop-in replacement yielding sub-second execution instead of 170s LLM chains
workflow = CompiledWorkflow()
final_state = workflow.execute({"query": "Find user records in database"})
```
* **PDF Link:** [Direct PDF Link](https://arxiv.org/pdf/2611.14492v1)

---

### [AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models](https://arxiv.org/abs/2611.14515v1)
* **Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li
* **The 30-Second Summary:** Standard Reinforcement Learning with Verifiable Rewards (RLVR) relies on crude binary pass/fail scores that discard rich learning signals. *AutoScaffold* introduces an automated training architecture where a frozen teacher model dynamically generates custom hints and scaffolding when a student model struggles, gradually fading them away as the student masters the domain.
* **The Breakthrough Explained:** Manually crafting intermediate hints and step-by-step scaffolds for custom enterprise reasoning or coding tasks does not scale. *AutoScaffold* solves this by implementing a teacher-student training feedback loop. When the student model hits a performance bottleneck, the teacher model inspects the failure state, writes targeted contextual hints on the fly to bridge the reasoning gap, and automatically removes the scaffolding once competence is established, accelerating model convergence.
* **🛠️ How You Can Apply This (Developer Takeaway):** When fine-tuning open-source models (Llama-3, Mistral) via RL or DPO on complex internal workflows, implement a dynamic curriculum dataset wrapper that injects AI-generated hints during early epochs:

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class TrainingSample:
    prompt: str
    target: str
    difficulty_score: float

class AutoScaffoldDataset:
    def __init__(self, teacher_model, student_eval_metric):
        self.teacher = teacher_model
        self.eval_metric = eval_metric

    def get_enhanced_prompt(self, sample: TrainingSample, student_success_rate: float) -> str:
        """Dynamically scaffolds hard samples based on student performance."""
        if student_success_rate < 0.4 and sample.difficulty_score > 0.7:
            # Teacher generates a targeted hint on the fly
            hint = self.teacher.generate(f"Provide a subtle hint for solving: {sample.prompt}")
            return f"Context/Hint: {hint}\n\nTask: {sample.prompt}"
        
        # Fade scaffolding as student competence increases
        return sample.prompt
```
* **PDF Link:** [Direct PDF Link](https://arxiv.org/pdf/2611.14515v1)

---

### [FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking](https://arxiv.org/abs/2611.14477v1)
* **Authors:** Arjun Rao, Nishant Gopinath
* **The 30-Second Summary:** Text-to-SQL agents over massive relational databases struggle with schema context windows and high latency when using expensive frontier LLMs for table retrieval. *FERN* eliminates generative LLMs from the retrieval phase entirely, fusing multiple frozen embedding retrievers with a lightweight gradient-boosted decision tree (`LightGBM`) to rank candidate schemas in milliseconds.
* **The Breakthrough Explained:** Instead of relying on a frontier model to parse keywords and filter through thousands of database schemas, *FERN* casts a wide net using three cheap, frozen embedding models. It then extracts up to 120 structural features for each candidate table and feeds them into a `LightGBM` ranker. This achieves near state-of-the-art table selection accuracy with a median latency of just 208 ms on a single A100 GPU and zero hosted generative model calls for the retrieval step.
* **🛠️ How You Can Apply This (Developer Takeaway):** Decouple your Text-to-SQL pipeline by replacing LLM-based schema selection with a high-speed feature extraction and ranking ensemble:

```python
import lightgbm as lgb
import numpy as np
from typing import List, Dict

class TableRankerPipeline:
    def __init__(self, lgb_model_path: str):
        # Load lightweight gradient-boosted decision tree ranker
        self.ranker = lgb.Booster(model_file=lgb_model_path)
        
    def extract_features(self, user_question: str, table_schema: Dict) -> np.ndarray:
        """Extracts structural features (e.g., name overlap, foreign keys, embedding similarity)."""
        features = [
            len(set(user_question.lower().split()).intersection(set(table_schema['name'].lower().split()))),
            float(table_schema.get('column_count', 0)),
            table_schema.get('embedding_cosine_similarity', 0.0),
            float(table_schema.get('has_foreign_keys', False))
        ]
        return np.array(features)

    def retrieve_top_tables(self, user_question: str, candidate_tables: List[Dict], top_k: int = 5) -> List[Dict]:
        X = np.array([self.extract_features(user_question, t) for t in candidate_tables])
        scores = self.ranker.predict(X)
        
        ranked_indices = np.argsort(scores)[::-1][:top_k]
        return [candidate_tables[i] for i in ranked_indices]

# Ultra-low latency (<250ms) zero-LLM retrieval phase before sending schema to SQL generator
pipeline = TableRankerPipeline("ferns_ranker.txt")
selected_tables = pipeline.retrieve_top_tables("Show total revenue by region", candidate_pool)
```
* **PDF Link:** [Direct PDF Link](https://arxiv.org/pdf/2611.14477v1)

---

### 💡 Builder Trend of the Day
The common thread across all three breakthroughs is **systematic de-escalation of runtime LLM dependency in favor of compiled, specialized, or deterministic architectures**. Whether it's replacing dynamic agentic planning loops with compiled execution code (*ReTrace*), replacing crude binary reinforcement learning rewards with AI-guided teacher scaffolding (*AutoScaffold*), or replacing expensive frontier model schema lookups with lightweight boosted decision trees (*FERN*), the industry is shifting away from unconstrained runtime inference. Applied AI engineering in 2026 is about using large models to *build, scaffold, and train* deterministic software systems rather than letting them guess their way through production loops in real-time.