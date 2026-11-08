# crew_polisher.py
import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

from crewai import Agent, Task, Crew, Process, LLM
from repo_auditor import audit_repo

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
    target_path = sys.argv[1] if len(sys.argv) > 1 else os.getenv("TARGET_REPO_PATH", "../ai-news-agent")
    
    print(f"Auditing repository at: {target_path}...")
    audit_data = audit_repo(target_path)
    print(f"Audit completed for '{audit_data['repo_name']}'.")

    payload = json.dumps(audit_data, indent=2, ensure_ascii=False)

    # 1. Auditor Agent
    auditor = Agent(
        role="Repository Quality Auditor",
        goal="Identify documentation deficiencies, missing badges, architecture gaps, and usability hurdles",
        backstory=(
            "You are a GitHub stars expert and open-source evaluator. You inspect repositories "
            "and identify what's missing: bad README formatting, lack of quickstart steps, missing architecture "
            "diagrams, or vague descriptions that turn users away."
        ),
        llm=llm,
        verbose=True
    )

    # 2. README Architect
    architect = Agent(
        role="Principal Documentation Architect",
        goal="Write a visually stunning, comprehensive, production-grade README.md file in Markdown",
        backstory=(
            "You write READMEs that get trending on GitHub. You include shields.io badges, "
            "clear problem explanations, interactive Mermaid architecture diagrams, copy-pasteable "
            "installation instructions, environment configuration tables, and contributing guidelines."
        ),
        llm=llm,
        verbose=True
    )

    # 3. Portfolio Spotlight Agent
    spotlight = Agent(
        role="Developer Portfolio Strategist",
        goal="Create a high-impact project summary snippet designed for the developer's main GitHub profile README",
        backstory=(
            "You know how tech recruiters and hiring managers skim GitHub profile READMEs. "
            "You craft concise 3-bullet project cards that highlight tech stack, engineering complexity, "
            "and practical value."
        ),
        llm=llm,
        verbose=True
    )

    t1 = Task(
        description=(
            f"Here is the audit data for the repository:\n{payload}\n\n"
            "Analyze the project and outline:\n"
            "1. Missing documentation components (e.g. badges, diagram, configuration guide)\n"
            "2. What makes this project technically interesting and how to highlight it\n"
            "3. Specific setup instructions based on the dependencies and file structure"
        ),
        expected_output="Audit report and structural plan for the new README.",
        agent=auditor
    )

    t2 = Task(
        description=(
            "Generate the complete, ultimate README.md for this repository.\n"
            "Must include:\n"
            "- Shields.io badges at the top (Python/Tech, License, GitHub stars placeholder)\n"
            "- 1-paragraph elevator pitch with emojis\n"
            "- Key Features (scannable bullet points)\n"
            "- Architecture Diagram (in clean ```mermaid format)\n"
            "- Tech Stack Breakdown table\n"
            "- Quickstart & Installation (step-by-step commands)\n"
            "- Environment Variables table (variable name, type, description, example)\n"
            "- How to run / usage examples\n"
            "- Roadmap & Contributing section\n"
            "- License"
        ),
        expected_output="A complete, flawless Markdown README string.",
        agent=architect,
        context=[t1]
    )

    t3 = Task(
        description=(
            "Based on the project, create a 'Profile README Showcase Card' (Markdown).\n"
            "This card should be formatted to be pasted directly into a developer's GitHub profile README (username/username).\n"
            "Include:\n"
            "- Project name with anchor link\n"
            "- 1-line hook\n"
            "- Tech stack pill badges\n"
            "- 2-3 key technical highlights (e.g. 'Autonomous multi-agent orchestration', 'Automated resilience & fallback')"
        ),
        expected_output="Markdown snippet for personal GitHub profile.",
        agent=spotlight,
        context=[t1, t2]
    )

    crew = Crew(
        agents=[auditor, architect, spotlight],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        max_rpm=15,
        verbose=True
    )

    print("\nStarting Polisher Crew execution...")
    try:
        crew.kickoff()
    except Exception as e:
        raise SystemExit(f"Crew kickoff failed: {e}")

    # Save results
    with open("README_PROPOSED.md", "w", encoding="utf-8") as f:
        f.write(str(t2.output) if t2.output else "")

    with open("PROFILE_SHOWCASE_SNIPPET.md", "w", encoding="utf-8") as f:
        f.write(str(t3.output) if t3.output else "")

    print("\n Polishing Complete!")
    print(" Saved new README to: README_PROPOSED.md")
    print(" Saved profile showcase snippet to: PROFILE_SHOWCASE_SNIPPET.md")

if __name__ == "__main__":
    main()

