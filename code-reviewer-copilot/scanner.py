# scanner.py
import os
import re
import subprocess
from pathlib import Path

# Common high-risk patterns for API keys and tokens
SECRET_PATTERNS = [
    (r"(AIza[0-9A-Za-z-_]{35})", "Google Gemini/Maps API Key"),
    (r"(sk-[a-zA-Z0-9]{20,})", "OpenAI / Anthropic Secret Key"),
    (r"(ghp_[a-zA-Z0-9]{36})", "GitHub Personal Access Token"),
    (r"(AKIA[0-9A-Z]{16})", "AWS Access Key ID"),
    (r"(password\s*=\s*['\"][^'\"]{4,}['\"])", "Hardcoded Password"),
]

def scan_for_secrets(content: str) -> list:
    """Finds suspected secrets in code string."""
    found = []
    for pattern, name in SECRET_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            found.append(name)
    return found

def get_git_diff(target_dir: str) -> str:
    """Attempts to retrieve git diff (unstaged or staged or latest commit)."""
    try:
        # Check unstaged
        res = subprocess.run(["git", "-C", target_dir, "diff"], capture_output=True, text=True)
        diff = res.stdout.strip()
        if diff:
            return diff
            
        # Check staged
        res = subprocess.run(["git", "-C", target_dir, "diff", "--staged"], capture_output=True, text=True)
        diff = res.stdout.strip()
        if diff:
            return diff

        # Check last commit
        res = subprocess.run(["git", "-C", target_dir, "diff", "HEAD~1"], capture_output=True, text=True)
        diff = res.stdout.strip()
        if diff:
            return diff
    except Exception:
        pass
    return ""

POLYGLOT_EXTENSIONS = (
    ".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs", 
    ".cpp", ".c", ".h", ".hpp", ".cs", ".java", ".kt", 
    ".swift", ".dart", ".rb", ".php", ".sql", ".sh", ".ps1"
)

def load_code_context(target_path: str, max_chars: int = 15000) -> dict:
    """
    Loads code either from git diff or directly from files across multiple languages.
    """
    p = Path(target_path).resolve()
    if not p.exists():
        raise FileNotFoundError(f"Path does not exist: {target_path}")

    diff = ""
    source_files = {}

    if p.is_dir():
        diff = get_git_diff(str(p))
        if not diff:
            # Read top code files across any supported language
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in {".git", "venv", ".venv", "__pycache__", "node_modules", "target", "dist", "build"}]
                for f in files:
                    if f.lower().endswith(POLYGLOT_EXTENSIONS) and len(source_files) < 6:
                        fp = os.path.join(root, f)
                        try:
                            with open(fp, "r", encoding="utf-8", errors="ignore") as file_obj:
                                source_files[f] = file_obj.read(4000)
                        except Exception:
                            pass
    else:
        # Single file
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as file_obj:
                source_files[p.name] = file_obj.read(max_chars)
        except Exception:
            pass

    combined_text = diff if diff else "\n\n".join(f"=== {k} ===\n{v}" for k, v in source_files.items())
    suspected_secrets = scan_for_secrets(combined_text)

    return {
        "target": str(p),
        "is_diff": bool(diff),
        "suspected_secrets": suspected_secrets,
        "code_content": combined_text[:max_chars]
    }

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "../ai-news-agent/crew_news.py"
    data = load_code_context(target)
    print("Target:", data["target"])
    print("Is Diff:", data["is_diff"])
    print("Suspected Secrets:", data["suspected_secrets"])
    print("Content Length:", len(data["code_content"]))

