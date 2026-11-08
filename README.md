# 🤖 Autonomous AI Agent Suite

A collection of **7 production-ready multi-agent systems** built with **CrewAI** and **Google Gemini** to supercharge a developer's daily workflow, automate learning, and enhance technical portfolio visibility.

---

## 🚀 The Multi-Agent Ecosystem

| Agent | Purpose | Autopilot Schedule | Output |
| :--- | :--- | :--- | :--- |
| **[`ai-news-agent`](./ai-news-agent)** | Curates daily top AI breakthroughs & saves HTML digest | Daily @ 04:45 IST | Google Drive / Docs |
| **[`oss-contributor-scout`](./oss-contributor-scout)** | Polyglot issue scout & PR blueprint generator (Python, TS, Go, Rust) | Daily @ 06:30 IST | `contributions_digest.md` |
| **[`arxiv-digest-agent`](./arxiv-digest-agent)** | Tracks latest arXiv AI/CS papers & turns them into code patterns | Daily @ 05:30 IST | `arxiv_digest.md` |
| **[`job-radar-agent`](./job-radar-agent)** | Scans remote developer jobs & crafts tailored 3-sentence pitches | Weekly (Mondays) | `OPPORTUNITIES_RADAR.md` |
| **[`repo-polisher`](./repo-polisher)** | Audits repos, drafts modern READMEs + Mermaid diagrams & profile cards | On-Demand | `README_PROPOSED.md` |
| **[`tech-storyteller`](./tech-storyteller)** | Transforms codebases into Dev.to tutorials & viral LinkedIn/X posts | On-Demand | `generated_article.md` |
| **[`code-reviewer-copilot`](./code-reviewer-copilot)** | AppSec & Staff Engineer code reviews for bugs & leaked secrets | On-Demand / PR | `CODE_REVIEW_REPORT.md` |
| **[`second-brain-archivist`](./second-brain-archivist)** | Diagnoses terminal errors, provides one-liner fixes & updates TIL log | On-Demand | `vault/` & `TIL_LOG.md` |

---

## ⚙️ Automated GitHub Actions

The autonomous agents run on GitHub Actions cron schedules and commit their updated digests automatically:
- **Daily Activity:** Green contribution streak updated with real AI digests and PR blueprints.
- **Manual Trigger:** Go to **Actions** tab on GitHub, pick any workflow, and click **Run workflow**.

---

## 🛠️ Quickstart (Local)

### 1. Prerequisites
- Python 3.11+
- Google Gemini API Key

### 2. Setup
```powershell
# Create & activate environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install requirements for any agent (e.g. oss-contributor-scout)
pip install -r oss-contributor-scout\requirements.txt
```

### 3. Environment Variables
Add your `GEMINI_API_KEY` to each agent's `.env` file (or set it globally).

