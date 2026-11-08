# ✍️ Tech Storyteller & Article Generator

An autonomous multi-agent Crew that inspects any local codebase, decodes its system architecture, and turns it into a **publication-ready technical blog post and viral social media launch posts (LinkedIn & X)**.

---

## 💡 Why This Agent?

- **Eases Your Life:** Writing articles and social posts about your projects takes hours of manual effort. This agent generates them automatically directly from your actual code.
- **Enhances Your Profile:** Transforms your raw code and hidden GitHub repos into visible thought leadership on Dev.to, Medium, LinkedIn, and Twitter.

---

## 🤖 The Multi-Agent Architecture

```mermaid
flowchart LR
    A[codebase_analyzer.py\nFile Tree & Code Scanner] --> B[Systems Analyst\nReverse-Engineers Architecture]
    B --> C[Technical Writer\nDrafts In-Depth Article]
    C --> D[DevRel Strategist\nCreates LinkedIn & X Posts]
    D --> E[generated_article.md\nsocial_posts.md]
```

1. **Principal Systems Analyst:** Extracts data flows, tool choices, error-handling patterns, and project purpose.
2. **Senior Technical Writer:** Drafts a full markdown article with problem statement, system walkthrough, code snippets, and takeaways.
3. **DevRel & Social Media Strategist:** Crafts punchy, ready-to-post copy for LinkedIn and Twitter with hooks and hashtags.

---

## 🚀 Quickstart

### 1. Installation

```powershell
# In E:\projects\AiAgentS\tech-storyteller
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env`:

```powershell
cp .env.example .env
```

Set:
- `GEMINI_API_KEY`: Your Gemini API key.
- `TARGET_REPO_PATH`: Path to any project you want to write about (e.g. `../ai-news-agent` or `../oss-contributor-scout`).

### 3. Run the Agent

You can point it to any directory either via `.env` or as a CLI argument:

```powershell
python crew_storyteller.py ../ai-news-agent
```

### 4. Output Files

- `generated_article.md`: Ready to paste into Dev.to, Hashnode, or Medium.
- `social_posts.md`: Ready to paste into LinkedIn and X.

