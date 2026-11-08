---
category: python
title: Fix CrewAI ImportError Cannot Import Name LLM
tags: [python, crewai, ai, pip, importerror, LLM]
---

# Fix CrewAI ImportError Cannot Import Name LLM

### 🚨 Error Signature
```text
ImportError: cannot import name 'LLM' from 'crewai'
```

### 🔍 Root Cause
This error occurs due to a version mismatch or breaking change where the installed `crewai` package is outdated and does not expose the `LLM` class at the top-level namespace (`from crewai import LLM`), or the codebase is targeting a different version than what is locally installed.

### ⚡ The Fix
Upgrade the `crewai` package to the latest version that natively supports top-level imports:

```bash
pip install --upgrade crewai
```

Alternatively, if pinned to an older version, adjust the import path directly:
```python
from crewai.agents.agent_builder.base_agent import LLM
```

### 🛡️ Prevention Rule
Always pin compatible library versions in `requirements.txt` or `pyproject.toml` when using rapidly evolving AI frameworks like CrewAI to prevent breaking changes from unexpected upstream updates.