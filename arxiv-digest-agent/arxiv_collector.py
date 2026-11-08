# arxiv_collector.py
import urllib.request
import xml.etree.ElementTree as ET
import re

ATOM_NS = "{http://www.w3.org/2005/Atom}"

def clean_text(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()

def fetch_recent_papers(query: str = "cat:cs.AI OR cat:cs.CL OR cat:cs.SE", max_results: int = 12) -> list:
    """
    Fetches the latest research papers from arXiv matching the given query categories.
    """
    encoded_query = urllib.parse.quote(query)
    url = (
        f"http://export.arxiv.org/api/query?"
        f"search_query={encoded_query}&"
        f"sortBy=submittedDate&"
        f"sortOrder=descending&"
        f"max_results={max_results}"
    )

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ArXiv-Digest-Agent/1.0"})
        with urllib.request.urlopen(req, timeout=20) as response:
            xml_data = response.read()

        root = ET.fromstring(xml_data)
        entries = root.findall(f"{ATOM_NS}entry")

        papers = []
        for entry in entries:
            title = clean_text(entry.find(f"{ATOM_NS}title").text)
            summary = clean_text(entry.find(f"{ATOM_NS}summary").text)
            published = clean_text(entry.find(f"{ATOM_NS}published").text)
            
            # Extract links
            arxiv_id = ""
            pdf_link = ""
            for link in entry.findall(f"{ATOM_NS}link"):
                href = link.attrib.get("href", "")
                rel = link.attrib.get("rel", "")
                title_attr = link.attrib.get("title", "")
                if rel == "alternate":
                    arxiv_id = href
                elif title_attr == "pdf" or "pdf" in href:
                    pdf_link = href

            # Extract authors
            authors = []
            for author in entry.findall(f"{ATOM_NS}author"):
                name = author.find(f"{ATOM_NS}name")
                if name is not None and name.text:
                    authors.append(name.text.strip())

            papers.append({
                "title": title,
                "url": arxiv_id,
                "pdf_url": pdf_link,
                "published": published[:10] if published else "",
                "authors": authors[:4],
                "abstract": summary[:1800]
            })

        return papers
    except Exception as e:
        print(f"Error fetching from arXiv: {e}")
        return []

if __name__ == "__main__":
    print("Testing arXiv collector...")
    results = fetch_recent_papers(max_results=3)
    print(f"Retrieved {len(results)} papers:")
    for p in results:
        print(f"- {p['title']} ({p['published']})\n  URL: {p['url']}")

