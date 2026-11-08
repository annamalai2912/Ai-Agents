# crew_arxiv.py
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from crewai import Agent, Task, Crew, Process
try:
    from crewai import LLM
except (ImportError, AttributeError):
    from crewai.llm import LLM
from arxiv_collector import fetch_recent_papers
from drive_sync import save_to_drive

gemini_model = os.getenv("GEMINI_MODEL", "gemini/gemini-3.5-flash-lite")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please set it in your .env file.")

llm = LLM(
    model=gemini_model,
    api_key=gemini_api_key,
    temperature=0.2,
)

def main():
    category_query = os.getenv("ARXIV_QUERY", "cat:cs.AI OR cat:cs.CL OR cat:cs.SE")
    max_papers = int(os.getenv("MAX_PAPERS", "12"))

    print(f"Fetching latest arXiv papers for: '{category_query}'...")
    candidates = fetch_recent_papers(query=category_query, max_results=max_papers)

    if not candidates:
        print("No papers retrieved. Check your network or query.")
        return

    print(f"Retrieved {len(candidates)} candidate papers. Running multi-agent synthesis...")
    payload = json.dumps(candidates, indent=2, ensure_ascii=False)

    # 1. Curator Agent
    curator = Agent(
        role="AI Research Curator",
        goal="Select the 3 most breakthrough, builder-relevant, and practical AI papers from candidates",
        backstory=(
            "You are an AI research engineer. You read dozens of papers daily and have an instinct for "
            "separating speculative, non-reproducible academic math from genuinely transformative techniques "
            "that software engineers and agent builders can use today."
        ),
        llm=llm,
        verbose=True
    )

    # 2. Deconstruction Analyst
    analyst = Agent(
        role="Research Deconstruction Analyst",
        goal="Extract the core breakthrough, eliminating academic jargon and explaining the key idea in plain English",
        backstory=(
            "You translate complex research into crystal-clear conceptual models. "
            "You explain the exact limitation of existing methods and how this new paper solves it."
        ),
        llm=llm,
        verbose=True
    )

    # 3. Practical Implementation Architect
    architect = Agent(
        role="Applied AI Implementation Architect",
        goal="Show how a software developer can apply these paper insights in code today, producing a polished Markdown digest",
        backstory=(
            "You are a pragmatic software builder. For every great research paper, you write a conceptual "
            "code snippet, prompt pattern, or architecture diagram showing how to adopt it in production."
        ),
        llm=llm,
        verbose=True
    )

    t1 = Task(
        description=(
            f"Here are candidate arXiv papers:\n{payload}\n\n"
            "Select the TOP 3 most valuable papers for an applied AI software engineer. "
            "For each selected paper, justify why it matters right now."
        ),
        expected_output="Selection of 3 standout papers with builder rationale.",
        agent=curator
    )

    t2 = Task(
        description=(
            "For each of the 3 selected papers, provide a 3-part breakdown:\n"
            "1. **The Core Problem:** What bottleneck or limitation in current AI does this paper address?\n"
            "2. **The Key Breakthrough:** How does their method work in simple, intuitive terms?\n"
            "3. **Real-world Results:** What benchmark or qualitative improvement was achieved?"
        ),
        expected_output="Deconstructed insights for all 3 papers.",
        agent=analyst,
        context=[t1]
    )

    t3 = Task(
        description=(
            "Format the entire research digest into a gorgeous, readable Markdown file:\n"
            "# 🧠 Daily AI Research Digest ({today})\n"
            "For each paper include:\n"
            "- ### [Paper Title](arXiv link)\n"
            "- **Authors:** list\n"
            "- **The 30-Second Summary:** (2 sentences)\n"
            "- **The Breakthrough Explained:**\n"
            "- **🛠️ How You Can Apply This (Developer Takeaway):** Include a short architecture pattern or Python code concept\n"
            "- **PDF Link:** direct link to pdf\n"
            "End with a '💡 Builder Trend of the Day' summarizing what all 3 papers reveal about where AI is heading."
        ).format(today=datetime.now().strftime("%Y-%m-%d")),
        expected_output="Final Markdown digest.",
        agent=architect,
        context=[t1, t2]
    )

    crew = Crew(
        agents=[curator, analyst, architect],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        max_rpm=15,
        verbose=True
    )

    try:
        crew.kickoff()
    except Exception as e:
        raise SystemExit(f"Crew kickoff failed: {e}")

    output_filename = "arxiv_digest.md"
    digest_text = str(t3.output) if t3.output else ""
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(digest_text)

    print(f"\n Synthesis complete! Digest saved to: {output_filename}")
    save_to_drive(digest_text, "ArXiv AI Research")

if __name__ == "__main__":
    main()

