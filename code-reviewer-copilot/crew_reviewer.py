# crew_reviewer.py
import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

from crewai import Agent, Task, Crew, Process, LLM
from scanner import load_code_context

gemini_model = os.getenv("GEMINI_MODEL", "gemini/gemini-3.5-flash-lite")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please set it in your .env file.")

llm = LLM(
    model=gemini_model,
    api_key=gemini_api_key,
    temperature=0.1,
)

def main():
    target_path = sys.argv[1] if len(sys.argv) > 1 else os.getenv("TARGET_PATH", "../ai-news-agent")
    
    print(f"Analyzing code context at: {target_path}...")
    context = load_code_context(target_path)
    
    if not context["code_content"]:
        print("No code or git diff found to review.")
        return

    payload = json.dumps(context, indent=2, ensure_ascii=False)

    # 1. Security Specialist
    security_agent = Agent(
        role="AppSec & Security Engineer",
        goal="Detect credential leaks, injection risks, insecure deserialization, and environment vulnerabilities",
        backstory=(
            "You are a paranoid application security engineer. You inspect code for leaked API keys, "
            "unvalidated inputs, command injections, unsafe file writes, and sensitive data leakage."
        ),
        llm=llm,
        verbose=True
    )

    # 2. Staff Software Engineer
    staff_engineer = Agent(
        role="Senior Staff Software Engineer",
        goal="Audit code architecture, unhandled edge cases, performance bottlenecks, and maintainability",
        backstory=(
            "You have reviewed thousands of pull requests in production systems. You spot silent crashes, "
            "missing try/except blocks, unhandled API timeouts, memory leaks, and anti-patterns instantly."
        ),
        llm=llm,
        verbose=True
    )

    # 3. Lead PR Reviewer
    lead_reviewer = Agent(
        role="Lead Code Reviewer",
        goal="Synthesize an actionable, constructive Code Review Report with severity ratings and refactored snippets",
        backstory=(
            "You write world-class code reviews. You prioritize issues into CRITICAL, WARNING, and SUGGESTION, "
            "explaining why each change matters and providing concise code diffs."
        ),
        llm=llm,
        verbose=True
    )

    t1 = Task(
        description=(
            f"Here is the code context:\n{payload}\n\n"
            "Perform a security audit. Check:\n"
            "1. Hardcoded keys/secrets or unsafe environment variable usage\n"
            "2. Network/API security (timeouts, SSL verification, header leaks)\n"
            "3. Injection or path traversal risks\n"
            "Rate overall security posture: SAFE / CONCERN / CRITICAL."
        ),
        expected_output="Security audit findings with severity ratings.",
        agent=security_agent
    )

    t2 = Task(
        description=(
            "Review the code for engineering excellence:\n"
            "1. Edge cases (e.g. None returns, empty lists, connection timeouts)\n"
            "2. Error handling (are errors caught and logged gracefully?)\n"
            "3. Complexity & Performance (redundant calculations, unbounded loops)\n"
            "4. Code clarity and typing"
        ),
        expected_output="Reliability and performance findings.",
        agent=staff_engineer
    )

    t3 = Task(
        description=(
            "Generate a final, polished Markdown report: 'CODE_REVIEW_REPORT.md'.\n"
            "Include:\n"
            "# 🛡️ Code Review & Health Report\n"
            "- **Target:** {target}\n"
            "- **Executive Verdict:** (Ready to merge / Needs changes / Critical fixes required)\n"
            "- ### 🚨 Critical & High-Priority Fixes (if any)\n"
            "- ### ⚠️ Performance & Reliability Warnings\n"
            "- ### 💡 Suggested Refactors & Best Practices (with before/after code blocks)\n"
            "- **Scorecard:** (Security: X/10, Reliability: X/10, Readability: X/10)"
        ).format(target=context["target"]),
        expected_output="Final Markdown review report.",
        agent=lead_reviewer,
        context=[t1, t2]
    )

    crew = Crew(
        agents=[security_agent, staff_engineer, lead_reviewer],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        max_rpm=15,
        verbose=True
    )

    try:
        crew.kickoff()
    except Exception as e:
        raise SystemExit(f"Review failed: {e}")

    report_file = "CODE_REVIEW_REPORT.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(str(t3.output) if t3.output else "")

    print(f"\n Review Complete! Report saved to: {report_file}")

if __name__ == "__main__":
    main()

