# github_scout.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = "https://api.github.com"

def get_headers():
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "OSS-Contributor-Scout-Agent"
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def search_issues_for_language(lang: str = "", topic: str = "", limit: int = 5):
    """Searches issues for a single language."""
    headers = get_headers()
    query_parts = [
        "is:issue",
        "is:open",
        "no:assignee",
        "archived:false",
        'label:"good first issue","help wanted"',
    ]
    if lang.strip():
        query_parts.append(f"language:{lang.strip()}")
    if topic.strip():
        query_parts.append(f"topic:{topic.strip()}")

    query = " ".join(query_parts)
    params = {
        "q": query,
        "sort": "updated",
        "order": "desc",
        "per_page": limit
    }
    
    try:
        response = requests.get(
            f"{GITHUB_API_URL}/search/issues",
            headers=headers,
            params=params,
            timeout=15
        )
        if response.status_code != 200:
            return []
        data = response.json()
        items = []
        for item in data.get("items", []):
            repo_api_url = item.get("repository_url", "")
            repo_name = "/".join(repo_api_url.split("/")[-2:]) if repo_api_url else "unknown"
            body = (item.get("body") or "").strip()
            if len(body) > 2000:
                body = body[:2000] + "\n...[truncated]"
            labels = [lbl.get("name", "") for lbl in item.get("labels", []) if isinstance(lbl, dict)]
            items.append({
                "id": item.get("id"),
                "number": item.get("number"),
                "title": item.get("title"),
                "repo": repo_name,
                "url": item.get("html_url"),
                "language": lang if lang else "polyglot",
                "labels": labels,
                "comments": item.get("comments", 0),
                "created_at": item.get("created_at"),
                "updated_at": item.get("updated_at"),
                "body": body
            })
        return items
    except Exception as e:
        print(f"Error fetching {lang} issues: {e}")
        return []

def fetch_candidate_issues(languages: str = "python,typescript,go,rust", topic: str = "", max_results: int = 15):
    """
    Finds open, unassigned issues across multiple programming languages.
    """
    lang_list = [l.strip() for l in languages.split(",") if l.strip()] if languages else [""]
    
    per_lang_limit = max(3, max_results // max(1, len(lang_list)))
    all_issues = []
    seen_ids = set()

    for lang in lang_list:
        results = search_issues_for_language(lang=lang, topic=topic, limit=per_lang_limit)
        for issue in results:
            if issue["id"] not in seen_ids:
                seen_ids.add(issue["id"])
                all_issues.append(issue)

    return all_issues[:max_results]

def get_repo_summary(repo_full_name: str) -> dict:
    """Fetches stats for a repository."""
    headers = get_headers()
    try:
        r = requests.get(f"{GITHUB_API_URL}/repos/{repo_full_name}", headers=headers, timeout=10)
        if r.status_code == 200:
            d = r.json()
            return {
                "name": repo_full_name,
                "stars": d.get("stargazers_count", 0),
                "forks": d.get("forks_count", 0),
                "description": d.get("description", ""),
                "open_issues": d.get("open_issues_count", 0),
                "language": d.get("language", "")
            }
    except Exception:
        pass
    return {"name": repo_full_name, "stars": "N/A", "description": ""}

if __name__ == "__main__":
    print("Testing Polyglot GitHub Scout...")
    results = fetch_candidate_issues(languages="python,typescript,go,rust", max_results=8)
    print(f"Found {len(results)} issues across languages:")
    for res in results:
        print(f"- [{res['language'].upper()}] [{res['repo']}] #{res['number']} {res['title']} ({res['url']})")
