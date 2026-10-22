
import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Tech Consultant - Knowledge Brain")

ARTICLES_FILE = Path(__file__).parent / "articles.json"


class Question(BaseModel):
    question: str


def load_articles():
    if not ARTICLES_FILE.exists():
        return []
    try:
        return json.loads(ARTICLES_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


@app.get("/")
def home():
    return {"message": "Knowledge Brain is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/query")
def query_knowledge(request: Question):
    question = request.question.strip()
    articles = load_articles()

    if not question:
        return {
            "question": question,
            "answer": "Please enter a question.",
            "sources": [],
            "needs_human": True
        }

    terms = set(question.lower().split())
    ranked = []

    for article in articles:
        text = article.get("text", "")
        title = article.get("title", "")
        searchable = f"{title} {text}".lower()
        score = sum(1 for term in terms if len(term) > 2 and term in searchable)

        if score:
            ranked.append((score, article))

    ranked.sort(key=lambda item: item[0], reverse=True)
    matches = ranked[:3]

    if not matches:
        return {
            "question": question,
            "answer": "I couldn't find a relevant article in the collected sample. Please contact a human support specialist.",
            "sources": [],
            "needs_human": True
        }

    sources = [
        {"title": item.get("title", "Support article"), "url": item.get("url", "")}
        for _, item in matches
    ]

    excerpts = [
        item.get("text", "")[:1200]
        for _, item in matches
    ]

    return {
        "question": question,
        "answer": "Relevant support article excerpts are provided below. This is keyword retrieval, not a Claude-generated answer:\n\n" + "\n\n".join(excerpts),
        "sources": sources,
        "needs_human": False
    }
