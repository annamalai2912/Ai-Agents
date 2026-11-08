# codebase_analyzer.py
import os
import subprocess
import json
from pathlib import Path

IGNORE_DIRS = {
    ".git", ".github", "venv", ".venv", "env", "__pycache__", 
    "node_modules", ".idea", ".vscode", "dist", "build"
}

ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".go", ".rs", ".java", 
    ".cpp", ".c", ".h", ".hpp", ".cs", ".kt", ".swift", ".dart",
    ".rb", ".php", ".md", ".json", ".yaml", ".yml", ".toml", ".txt", ".sql", ".sh"
}

def get_recent_git_commits(repo_path: str, count: int = 10) -> list:
    """Extracts recent git commit messages."""
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "log", f"-n {count}", "--oneline"],
            capture_output=True,
            text=True,
            check=True
        )
        return [line.strip() for line in result.stdout.strip().split("\n") if line.strip()]
    except Exception:
        return []

def scan_project(repo_path: str, max_files_read: int = 8, max_chars_per_file: int = 2500) -> dict:
    """
    Scans a local repository/project directory and extracts structural
    and source code context.
    """
    path = Path(repo_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {repo_path}")

    file_tree = []
    key_files_content = {}
    total_files = 0

    for root, dirs, files in os.walk(path):
        # Filter out ignored directories in-place
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
        
        rel_root = os.path.relpath(root, path)
        if rel_root == ".":
            rel_root = ""

        for file in files:
            total_files += 1
            rel_file_path = os.path.join(rel_root, file) if rel_root else file
            file_tree.append(rel_file_path)

            ext = os.path.splitext(file)[1].lower()
            if ext in ALLOWED_EXTENSIONS and len(key_files_content) < max_files_read:
                # Prioritize important entry points, crew files, configs, and README
                is_priority = (
                    "crew" in file.lower() or 
                    "main" in file.lower() or 
                    "agent" in file.lower() or 
                    file.lower() == "readme.md" or
                    "requirements" in file.lower() or 
                    "package.json" in file.lower()
                )
                if is_priority or len(key_files_content) < 3:
                    full_p = os.path.join(root, file)
                    try:
                        with open(full_p, "r", encoding="utf-8", errors="ignore") as f:
                            text = f.read(max_chars_per_file)
                            key_files_content[rel_file_path] = text
                    except Exception:
                        pass

    git_commits = get_recent_git_commits(str(path))

    return {
        "project_name": path.name,
        "project_path": str(path),
        "total_files": total_files,
        "file_tree": file_tree[:40],
        "git_commits": git_commits,
        "source_samples": key_files_content
    }

if __name__ == "__main__":
    import sys
    test_target = sys.argv[1] if len(sys.argv) > 1 else "../ai-news-agent"
    summary = scan_project(test_target)
    print("Project Name:", summary["project_name"])
    print("Total files found:", summary["total_files"])
    print("Files read:", list(summary["source_samples"].keys()))

