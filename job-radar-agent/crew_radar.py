# crew_radar.py
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from crewai import Agent, Task, Crew, Process, LLM
from job_fetcher import fetch_remote_programming_jobs
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

def load_skills():
    skills_path = "MY_SKILLS.md"
    if os.path.exists(skills_path):
        with open(skills_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Python, AI Agents, Backend Development, LLMs, FastAPI, Git."

def main():
    print("Loading candidate jobs from remote developer boards...")
    jobs = fetch_remote_programming_jobs(max_jobs=12)
    
    if not jobs:
        print("No job postings found.")
        return

    skills = load_skills()
    jobs_payload = json.dumps(jobs, indent=2, ensure_ascii=False)

    # 1. Opportunity Filter Agent
    filter_agent = Agent(
        role="Technical Career & Opportunity Scout",
        goal="Filter candidate jobs to identify the top 3-4 roles that closely match the developer's tech stack and preferences",
        backstory=(
            "You are an executive tech recruiter. You ignore enterprise buzzwords and identify real engineering roles "
            "where hands-on Python, AI systems, and autonomy are valued."
        ),
        llm=llm,
        verbose=True
    )

    # 2. Match Evaluator Agent
    evaluator_agent = Agent(
        role="Stack Fit Evaluator",
        goal="Score each match percentage, highlight skill alignments, and identify any missing gaps to brush up on",
        backstory=(
            "You evaluate job requirements against a developer's real capabilities. You assign realistic match percentages "
            "and point out exact talking points for interviews."
        ),
        llm=llm,
        verbose=True
    )

    # 3. Pitch Strategist Agent
    pitch_agent = Agent(
        role="Outreach & Pitch Strategist",
        goal="Draft punchy, custom 3-sentence application/outreach notes and format OPPORTUNITIES_RADAR.md",
        backstory=(
            "You write magnetic cold outreach messages. You avoid generic cover letter clichés and lead with "
            "relevant projects and immediate value."
        ),
        llm=llm,
        verbose=True
    )

    t1 = Task(
        description=(
            f"Here is the developer's skills profile:\n{skills}\n\n"
            f"Here are recent remote job openings:\n{jobs_payload}\n\n"
            "Select the top 3 or 4 positions that best match the developer's background in Python, AI, and backend systems."
        ),
        expected_output="Curated list of 3-4 best-matching job openings.",
        agent=filter_agent
    )

    t2 = Task(
        description=(
            "For each selected job, provide:\n"
            "1. **Match Score (%):** (e.g. 88%)\n"
            "2. **Why You Match:** 2-3 specific overlap points between your skills and the role requirements\n"
            "3. **Skill Gaps:** Any secondary tools mentioned that you could quickly learn"
        ),
        expected_output="Match evaluation breakdown per role.",
        agent=evaluator_agent,
        context=[t1]
    )

    t3 = Task(
        description=(
            "Generate the final Markdown digest 'OPPORTUNITIES_RADAR.md':\n"
            "# 🎯 Remote Tech Opportunity Radar ({today})\n\n"
            "For each matched role:\n"
            "- ### [Company] Role Title (Link)\n"
            "- **Match Score:** X%\n"
            "- **Key Overlap:** Bullet points\n"
            "- **Missing / Growth Skills:** Note\n"
            "- **Tailored 3-Sentence Pitch:** A direct outreach message ready to send to the founder or hiring manager.\n\n"
            "End with a '💡 Portfolio Recommendation' on what small demo project would make the developer irresistible for these roles."
        ).format(today=datetime.now().strftime("%Y-%m-%d")),
        expected_output="Final Markdown digest.",
        agent=pitch_agent,
        context=[t1, t2]
    )

    crew = Crew(
        agents=[filter_agent, evaluator_agent, pitch_agent],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        max_rpm=15,
        verbose=True
    )

    try:
        crew.kickoff()
    except Exception as e:
        raise SystemExit(f"Radar run failed: {e}")

    output_file = "OPPORTUNITIES_RADAR.md"
    radar_text = str(t3.output) if t3.output else ""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(radar_text)

    print(f"\n Opportunity scan complete! Digest saved to: {output_file}")
    save_to_drive(radar_text, "Remote Tech Opportunities")

if __name__ == "__main__":
    main()

