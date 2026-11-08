# job_fetcher.py
import re
import feedparser

WWR_PROGRAMMING_FEED = "https://weworkremotely.com/categories/remote-programming-jobs.rss"

def clean_html(raw_html: str) -> str:
    clean = re.sub(r"<[^>]+>", " ", raw_html or "")
    return re.sub(r"\s+", " ", clean).strip()

def fetch_remote_programming_jobs(max_jobs: int = 15) -> list:
    """
    Fetches live remote developer job openings via public RSS.
    """
    try:
        feed = feedparser.parse(WWR_PROGRAMMING_FEED)
        jobs = []
        for entry in feed.entries[:max_jobs]:
            title = entry.get("title", "")
            company = ""
            role_title = title
            if ":" in title:
                parts = title.split(":", 1)
                company = parts[0].strip()
                role_title = parts[1].strip()

            summary = clean_html(entry.get("summary", ""))
            
            jobs.append({
                "company": company,
                "role": role_title,
                "url": entry.get("link", ""),
                "published": entry.get("published", "")[:16],
                "description_preview": summary[:1200]
            })

        return jobs
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []

if __name__ == "__main__":
    print("Testing Job Fetcher...")
    results = fetch_remote_programming_jobs(max_jobs=4)
    print(f"Fetched {len(results)} jobs:")
    for j in results:
        print(f"- [{j['company']}] {j['role']}\n  URL: {j['url']}")

