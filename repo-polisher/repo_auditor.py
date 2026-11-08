# repo_auditor.py
import os
from pathlib import Path

IGNORE_DIRS = {".git", ".github", "venv", ".venv", "env", "__pycache__", "node_modules", "dist", "build"}

def audit_repo(repo_path: str) -> dict:
    """
    Audits a local repository to assess its documentation, tooling, and architecture.
    """
    p = Path(repo_path).resolve()
    if not p.exists():
        raise FileNotFoundError(f"Path not found: {repo_path}")

    files_list = []
    has_readme = False
    existing_readme = ""
    has_license = False
    has_env_example = False
    has_tests = False
    has_ci = False
    dependencies_content = ""
    code_samples = {}

    for root, dirs, files in os.walk(p):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
        rel_root = os.path.relpath(root, p)
        if rel_root == ".":
            rel_root = ""

        if ".github" in root and "workflows" in root:
            has_ci = True

        for file in files:
            rel_path = os.path.join(rel_root, file) if rel_root else file
            files_list.append(rel_path)
            lower_name = file.lower()

            if lower_name == "readme.md":
                has_readme = True
                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                        existing_readme = f.read(3000)
                except Exception:
                    pass

            elif "license" in lower_name:
                has_license = True
            elif ".env.example" in lower_name or ".env.sample" in lower_name:
                has_env_example = True
            elif "test" in lower_name or "tests" in rel_root.lower():
                has_tests = True
            elif lower_name in ["requirements.txt", "pyproject.toml", "package.json", "go.mod", "cargo.toml", "pom.xml", "build.gradle", "cmakelists.txt", "gemfile", "composer.json"]:
                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                        dependencies_content += f"\n--- {file} ---\n" + f.read(1500)
                except Exception:
                    pass
            elif lower_name.endswith((".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs", ".java", ".cpp", ".c", ".cs", ".kt", ".swift", ".rb", ".php")):
                if len(code_samples) < 5 and any(k in lower_name for k in ["main", "app", "crew", "agent", "server", "index", "lib"]):
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                            code_samples[rel_path] = f.read(2000)
                    except Exception:
                        pass

    return {
        "repo_name": p.name,
        "repo_path": str(p),
        "has_readme": has_readme,
        "has_license": has_license,
        "has_env_example": has_env_example,
        "has_tests": has_tests,
        "has_ci": has_ci,
        "dependencies": dependencies_content.strip(),
        "existing_readme": existing_readme,
        "file_tree": files_list[:40],
        "key_code_samples": code_samples
    }

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "../ai-news-agent"
    res = audit_repo(target)
    print(f"Audited {res['repo_name']}:")
    print(f"- Has README: {res['has_readme']}")
    print(f"- Has License: {res['has_license']}")
    print(f"- Has CI: {res['has_ci']}")
    print(f"- Files inspected: {len(res['file_tree'])}")

