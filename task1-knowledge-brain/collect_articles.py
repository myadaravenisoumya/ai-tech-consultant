
import json
from pathlib import Path
import xml.etree.ElementTree as ET

import httpx
from bs4 import BeautifulSoup

SITEMAP_URL = "https://support.brilliantdirectories.com/support/sitemap.xml"
OUTPUT_FILE = Path(__file__).parent / "articles.json"


def main():
    articles = []

    try:
        with httpx.Client(
            timeout=10,
            follow_redirects=True,
            headers={"User-Agent": "AI-Tech-Consultant/1.0"}
        ) as client:
            print("Downloading sitemap...", flush=True)
            response = client.get(SITEMAP_URL)
            response.raise_for_status()

            root = ET.fromstring(response.content)
            urls = [
                element.text.strip()
                for element in root.iter()
                if element.tag.endswith("loc") and element.text
            ]

            print(f"Found {len(urls)} URLs.", flush=True)

            # Test only five URLs first.
            for index, url in enumerate(urls[:5], start=1):
                try:
                    print(f"Reading article {index}/5...", flush=True)
                    page = client.get(url)
                    page.raise_for_status()

                    soup = BeautifulSoup(page.text, "html.parser")

                    for tag in soup.select(
                        "script, style, nav, footer, header, noscript"
                    ):
                        tag.decompose()

                    content = (
                        soup.find("main")
                        or soup.find("article")
                        or soup.body
                    )

                    text = content.get_text(" ", strip=True) if content else ""
                    title = (
                        soup.title.get_text(" ", strip=True)
                        if soup.title else url
                    )

                    if text:
                        articles.append({
                            "url": url,
                            "title": title,
                            "text": text
                        })

                except Exception as error:
                    print(f"Article skipped: {error}", flush=True)

    except Exception as error:
        print(f"Collector failed: {error}", flush=True)

    OUTPUT_FILE.write_text(
        json.dumps(articles, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    print(f"Saved {len(articles)} articles to {OUTPUT_FILE}", flush=True)


if __name__ == "__main__":
    main()
