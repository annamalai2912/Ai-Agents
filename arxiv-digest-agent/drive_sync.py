# drive_sync.py
import os
import requests
import markdown
from datetime import datetime, timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))

def save_to_drive(md_text: str, doc_title: str):
    """
    Uploads a markdown digest to Google Drive via Google Apps Script Webhook.
    """
    url = os.getenv("DRIVE_WEBHOOK_URL")
    secret = os.getenv("DRIVE_SECRET")
    
    if not (url and secret):
        print("Google Drive webhook not configured; skipping upload.")
        return False
        
    try:
        html_content = markdown.markdown(md_text)
        payload = {
            "secret": secret,
            "title": f"{doc_title} {datetime.now(IST).strftime('%Y-%m-%d')}",
            "html": html_content
        }
        r = requests.post(url, json=payload, timeout=60)
        print("Drive upload response:", r.text)
        return True
    except Exception as e:
        print(f"Error uploading to Drive: {e}")
        return False

