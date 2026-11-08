# crew_archivist.py
import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

from crewai import Agent, Task, Crew, Process
try:
    from crewai import LLM
except (ImportError, AttributeError):
    from crewai.llm import LLM
from vault_manager import save_entry_to_vault

gemini_model = os.getenv("GEMINI_MODEL", "gemini/gemini-3.5-flash-lite")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please set it in your .env file.")

llm = LLM(
    model=gemini_model,
    api_key=gemini_api_key,
    temperature=0.1,
)

def load_input_text(file_path: str = "input.txt") -> str:
    if len(sys.argv) > 1:
        # Check if first arg is an existing file
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        return " ".join(sys.argv[1:])
    
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    
    return ""

def main():
    raw_problem = load_input_text()
    if not raw_problem.strip():
        print("Please provide an error message or snippet in 'input.txt' or as a command-line argument.")
        return

    print("Analyzing and archiving error/problem log...")

    # 1. Root Cause Detective
    detective = Agent(
        role="Root Cause Debugging Detective",
        goal="Parse chaotic terminal output, stack traces, or error logs to isolate the exact technical root cause",
        backstory=(
            "You are a systems troubleshooter. You cut through 200 lines of traceback noise to pinpoint "
            "the single missing package, permission flag, version mismatch, or typo causing the crash."
        ),
        llm=llm,
        verbose=True
    )

    # 2. Fix Engineer
    fix_engineer = Agent(
        role="Pragmatic Fix Engineer",
        goal="Provide the minimal, most reliable command or code change to resolve the issue permanently",
        backstory=(
            "You provide clean, tested, reproducible fixes. You don't give 10 vague possibilities; you give "
            "the exact one-liner terminal command or code diff that fixes it."
        ),
        llm=llm,
        verbose=True
    )

    # 3. Knowledge Base Curator
    curator = Agent(
        role="Second-Brain Knowledge Curator",
        goal="Structure the problem, solution, category, and prevention rule into a clean Markdown note and JSON metadata",
        backstory=(
            "You maintain technical wikis and personal knowledge vaults (Obsidian / GitHub TIL). "
            "You structure notes so that searching for the error signature in 6 months instantly yields the exact fix."
        ),
        llm=llm,
        verbose=True
    )

    t1 = Task(
        description=(
            f"Here is the raw error or problem input:\n```\n{raw_problem[:4000]}\n```\n\n"
            "Analyze and explain:\n"
            "1. What is the core error signature?\n"
            "2. What is the actual underlying technical reason it occurred?"
        ),
        expected_output="Root cause explanation and error signature.",
        agent=detective
    )

    t2 = Task(
        description=(
            "Provide the exact, step-by-step fix:\n"
            "- Exact terminal command or code patch\n"
            "- Why this resolves it\n"
            "- How to verify it works"
        ),
        expected_output="Exact resolution steps and commands.",
        agent=fix_engineer,
        context=[t1]
    )

    t3 = Task(
        description=(
            "Create the final archival entry.\n"
            "Produce a markdown document with this format:\n"
            "---\n"
            "category: (one of: python, typescript, javascript, go, rust, cpp, java, docker, kubernetes, git, database, linux, windows, ai, mobile)\n"
            "title: (Clear descriptive title e.g. Fix Google GenAI gRPC DLL Load Failed)\n"
            "tags: [tag1, tag2]\n"
            "---\n\n"
            "# Title\n\n"
            "### 🚨 Error Signature\n"
            "```text\n(brief snippet of error)\n```\n\n"
            "### 🔍 Root Cause\n(1-2 clear sentences)\n\n"
            "### ⚡ The Fix\n```powershell or code\n(the command or code)\n```\n\n"
            "### 🛡️ Prevention Rule\n(1 rule so this never happens again)\n"
        ),
        expected_output="Final structured markdown archive note with YAML frontmatter.",
        agent=curator,
        context=[t1, t2]
    )

    crew = Crew(
        agents=[detective, fix_engineer, curator],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        max_rpm=15,
        verbose=True
    )

    import time
    for attempt in range(3):
        try:
            crew.kickoff()
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < 2:
                print(f"Retrying in {(attempt + 1) * 15}s...")
                time.sleep((attempt + 1) * 15)
    else:
        raise SystemExit("Archival crew kickoff failed after 3 attempts.")

    result_text = str(t3.output) if t3.output else ""
    
    # Extract category and title from frontmatter if possible
    category = "general"
    title = "Solved Error"
    for line in result_text.split("\n"):
        if line.startswith("category:"):
            category = line.split(":", 1)[1].strip()
        elif line.startswith("title:"):
            title = line.split(":", 1)[1].strip()

    saved_path = save_entry_to_vault(category, title, result_text)
    print(f"\n Note permanently archived to: {saved_path}")
    print(f" Logged in: TIL_LOG.md")
    print("\n" + "="*50 + "\n" + result_text)

if __name__ == "__main__":
    main()

