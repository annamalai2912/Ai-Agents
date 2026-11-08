# vault_manager.py
import os
import re
from pathlib import Path
from datetime import datetime

VAULT_DIR = Path(__file__).parent / "vault"
TIL_LOG_FILE = Path(__file__).parent / "TIL_LOG.md"

def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)[:40]

def save_entry_to_vault(category: str, title: str, content: str) -> str:
    """
    Saves a structured note to the vault and appends to TIL_LOG.md
    """
    cat_clean = slugify(category) or "general"
    category_path = VAULT_DIR / cat_clean
    category_path.mkdir(parents=True, exist_ok=True)

    file_slug = slugify(title) or "note"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    note_filename = f"{timestamp}_{file_slug}.md"
    note_path = category_path / note_filename

    with open(note_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Append to TIL_LOG.md
    rel_path = f"vault/{cat_clean}/{note_filename}"
    log_line = f"- [{datetime.now().strftime('%Y-%m-%d')}] **[{category.upper()}]** [{title}]({rel_path})\n"

    if not TIL_LOG_FILE.exists():
        with open(TIL_LOG_FILE, "w", encoding="utf-8") as f:
            f.write("# 📚 Today I Learned (TIL) & Bug Fix Archive\n\nPersonal knowledge vault of solved errors, configurations, and engineering tricks.\n\n## 📝 Entries\n\n")

    with open(TIL_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line)

    return str(note_path)

if __name__ == "__main__":
    p = save_entry_to_vault("python", "Fix ModuleNotFoundError in subfolder", "# Fix ModuleNotFoundError\n\nAdd __init__.py")
    print(f"Saved sample note to: {p}")

