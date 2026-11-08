# crew_storyteller.py
import os
import sys
import json
import time
from dotenv import load_dotenv

load_dotenv()

from crewai import Agent, Task, Crew, Process, LLM
from codebase_analyzer import scan_project

gemini_model = os.getenv("GEMINI_MODEL", "gemini/gemini-3.5-flash-lite")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please set it in your .env file.")

llm = LLM(
    model=gemini_model,
    api_key=gemini_api_key,
    temperature=0.3,
)

def main():
    target_path = sys.argv[1] if len(sys.argv) > 1 else os.getenv("TARGET_REPO_PATH", "../ai-news-agent")
    
    print(f"Scanning codebase at: {target_path}...")
    project_data = scan_project(target_path)
    print(f"Scanned '{project_data['project_name']}'. Extracted {len(project_data['source_samples'])} source files.")
    
    payload = json.dumps(project_data, indent=2, ensure_ascii=False)

    # Agent 1: Technical Systems Analyst
    analyst = Agent(
        role="Principal Systems Analyst",
        goal="Reverse-engineer and explain the system architecture, design patterns, and engineering decisions of the codebase",
        backstory=(
            "You are a seasoned software architect and technical reviewer. You examine code, directory structures, "
            "and dependencies to determine the core problem the project solves, how data flows through the system, "
            "and why the engineering approach is effective."
        ),
        llm=llm,
        verbose=True
    )

    # Agent 2: Senior Technical Writer
    writer = Agent(
        role="Senior Technical Writer",
        goal="Write a publication-ready, deeply informative technical blog post that showcases the developer's engineering depth",
        backstory=(
            "You write top-ranking articles for publications like Towards Data Science, Dev.to, and HackerNoon. "
            "You avoid buzzword-heavy fluff and write engaging, hands-on tutorials with real code snippets, "
            "clear architecture diagrams, and lessons learned."
        ),
        llm=llm,
        verbose=True
    )

    # Agent 3: Developer Relations & Social Strategist
    social_strategist = Agent(
        role="DevRel & Social Media Strategist",
        goal="Turn the project into high-engagement LinkedIn and X (Twitter) launch posts to maximize developer visibility",
        backstory=(
            "You are a developer advocate who knows how to tell authentic engineering stories on social media. "
            "You hook readers with real challenges solved, share key takeaways in scannable bullet points, "
            "and build genuine technical credibility."
        ),
        llm=llm,
        verbose=True
    )

    t1 = Task(
        description=(
            f"Here is the scanned project data:\n{payload}\n\n"
            "Analyze the project and provide:\n"
            "1. Core problem statement & purpose\n"
            "2. Architecture & Data Flow (Step-by-step how the components interact)\n"
            "3. Key libraries & tools used and why they were chosen\n"
            "4. Notable code patterns, robustness features (e.g. retries, error handling, prompt engineering)"
        ),
        expected_output="Detailed architectural analysis of the project.",
        agent=analyst
    )

    t2 = Task(
        description=(
            "Based on the Architectural Analysis, write an engaging technical blog post in Markdown.\n"
            "Include:\n"
            "- Catchy, developer-friendly title (e.g. 'How I Built an Autonomous Multi-Agent AI System...')\n"
            "- The Problem / Motivation: Why build this?\n"
            "- Architecture & Workflow (include a Mermaid diagram if applicable)\n"
            "- Deep Dive: Key code highlights and agent interactions\n"
            "- Edge cases & Challenges solved (rate limits, context windows, error handling)\n"
            "- Key Takeaways & What's Next\n"
            "Format cleanly with markdown headers, code blocks, and clear explanations."
        ),
        expected_output="Complete, publication-ready markdown article.",
        agent=writer,
        context=[t1]
    )

    t3 = Task(
        description=(
            "Based on the project analysis and article, create:\n"
            "1. **LinkedIn Post**: A 250-350 word professional story: strong opening hook, the engineering problem, "
            "how it was solved, key metrics/takeaways, and relevant tech hashtags (#AI #Python #SoftwareEngineering).\n"
            "2. **X / Twitter Thread**: A 4-tweet thread breaking down the project with punchy insights, a code highlight, "
            "and a link placeholder.\n"
            "Format in Markdown under clear headers."
        ),
        expected_output="Markdown document containing the LinkedIn post and X thread.",
        agent=social_strategist,
        context=[t1, t2]
    )

    crew = Crew(
        agents=[analyst, writer, social_strategist],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        max_rpm=15,
        verbose=True
    )

    print("\nStarting Storyteller Crew execution...")
    try:
        crew.kickoff()
    except Exception as e:
        raise SystemExit(f"Crew kickoff failed: {e}")

    # Save outputs
    article_content = str(t2.output) if t2.output else ""
    social_content = str(t3.output) if t3.output else ""

    with open("generated_article.md", "w", encoding="utf-8") as f:
        f.write(article_content)

    with open("social_posts.md", "w", encoding="utf-8") as f:
        f.write(social_content)

    print("\n Generation Complete!")
    print(" Saved article to: generated_article.md")
    print(" Saved social posts to: social_posts.md")

if __name__ == "__main__":
    main()

