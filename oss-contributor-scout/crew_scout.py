# crew_scout.py
import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from crewai import Agent, Task, Crew, Process
try:
    from crewai import LLM
except (ImportError, AttributeError):
    from crewai.llm import LLM
from github_scout import fetch_candidate_issues, get_repo_summary
from drive_sync import save_to_drive

# Setup LLM with Google Gemini
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
    target_languages = os.getenv("TARGET_LANGUAGES", os.getenv("TARGET_LANGUAGE", "python,typescript,javascript,go,rust"))
    target_topic = os.getenv("TARGET_TOPIC", "")
    
    print(f"Scouting open-source issues for languages='{target_languages}', topic='{target_topic}'...")
    candidates = fetch_candidate_issues(
        languages=target_languages,
        topic=target_topic,
        max_results=12
    )
    
    if not candidates:
        print("No issues found matching the criteria. Try relaxing your filters in .env.")
        return

    # Augment candidates with repo stats for top candidates
    enriched = []
    for issue in candidates[:8]:
        repo_stats = get_repo_summary(issue["repo"])
        issue["repo_stars"] = repo_stats.get("stars", 0)
        issue["repo_description"] = repo_stats.get("description", "")
        enriched.append(issue)

    issues_payload = json.dumps(enriched, indent=2, ensure_ascii=False)

    # 1. Scout Agent: Picks the best 2-3 issues
    scout = Agent(
        role="Open Source Scout",
        goal="Select the 2-3 highest-signal, most feasible, and resume-boosting open-source issues from candidates",
        backstory=(
            "You are an experienced open-source mentor. You filter out poorly described issues, "
            "crypto/bounty spam, or trivial single-letter typo fixes. You pick issues in active repos "
            "where fixing the bug demonstrates genuine problem-solving skills that look great on a portfolio."
        ),
        llm=llm,
        verbose=True
    )

    # 2. Architect Agent: Develops the solution plan
    architect = Agent(
        role="PR Solution Architect",
        goal="Break down each selected issue into a clear technical root cause and step-by-step fix strategy",
        backstory=(
            "You are a principal engineer who quickly understands unfamiliar codebases. "
            "You explain which parts of the codebase to look at, the likely root cause, "
            "how to implement the fix safely, and what unit tests or verification steps to run."
        ),
        llm=llm,
        verbose=True
    )

    # 3. Coach Agent: Crafts maintainer pitches and formats the digest
    coach = Agent(
        role="Contribution & Pitch Coach",
        goal="Produce a professional Markdown digest with a ready-to-paste maintainer comment for each issue",
        backstory=(
            "You know how maintainers think. You compose polite, concise GitHub comments that explain "
            "you'd like to tackle the issue and summarize your planned approach so maintainers readily assign it to you."
        ),
        llm=llm,
        verbose=True
    )

    # Tasks
    t1 = Task(
        description=(
            f"Here are candidate GitHub issues in JSON format:\n{issues_payload}\n\n"
            "Analyze and select the TOP 2 or 3 best issues to tackle. For each selected issue, provide:\n"
            "- Repo & Issue Title and URL\n"
            "- Stars and why the repo is good for credibility\n"
            "- Why this specific issue is a good contribution opportunity\n"
            "Discard any issues that lack details, look abandoned, or are spam."
        ),
        expected_output="Curated list of 2-3 selected issues with justification.",
        agent=scout
    )

    t2 = Task(
        description=(
            "For each selected issue from the Scout, produce a technical solution blueprint:\n"
            "1. Problem summary (in simple engineering terms)\n"
            "2. Expected files/modules to inspect\n"
            "3. Step-by-step implementation plan\n"
            "4. Testing / verification strategy (e.g. pytest case to reproduce and test)"
        ),
        expected_output="Technical blueprint and implementation steps for each selected issue.",
        agent=architect,
        context=[t1]
    )

    t3 = Task(
        description=(
            "Compile everything into a clean, modern GitHub Markdown digest with:\n"
            "# 🚀 Open-Source Contribution Opportunities (Generated {date})\n"
            "For each issue include:\n"
            "- ### Issue Title with link & Repo star count\n"
            "- **Profile Value:** 1 sentence on why having this merged PR boosts your portfolio\n"
            "- **The Challenge:** Brief summary\n"
            "- **Technical Plan:** Step-by-step checklist\n"
            "- **Ready-to-Post Claim Comment:** In a markdown code block, a polite, professional comment "
            "the user can copy-paste to GitHub asking the maintainer to assign them the issue along with their proposed fix."
        ).format(date=datetime.now().strftime("%Y-%m-%d")),
        expected_output="Final Markdown document containing all sections.",
        agent=coach,
        context=[t1, t2]
    )

    crew = Crew(
        agents=[scout, architect, coach],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        max_rpm=15,
        verbose=True
    )

    print("\nStarting Crew execution...")
    output = None
    for attempt in range(3):
        try:
            output = str(crew.kickoff())
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(10 * (attempt + 1))
            
    if not output:
        raise SystemExit("Crew execution failed after 3 attempts.")

    # Save to file
    output_filename = "contributions_digest.md"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\n Success! Digest saved to {output_filename}")
    save_to_drive(output, "OSS Opportunities")
    print("\n" + "="*60 + "\n")
    print(output)

if __name__ == "__main__":
    main()

