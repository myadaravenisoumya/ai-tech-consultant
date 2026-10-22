from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI(title="Inbox Agent")

KNOWLEDGE_API = "http://127.0.0.1:8000/query"

class Email(BaseModel):
    subject: str
    body: str

@app.get("/health")
def health():
    return {"status": "healthy", "agent": "Inbox Agent"}

@app.post("/draft")
def draft(email: Email):
    question = f"{email.subject}\n{email.body}"

    try:
        response = httpx.post(
            KNOWLEDGE_API,
            json={"question": question},
            timeout=20
        )
        response.raise_for_status()
        knowledge = response.json()
    except Exception:
        return {
            "draft": "We are reviewing your request and will follow up.",
            "needs_human": True,
            "reason": "Knowledge service unavailable"
        }

    sources = knowledge.get("sources", [])
    if knowledge.get("needs_human") or not sources:
        return {
            "draft": "Thank you for contacting support. Our team will review your request and follow up.",
            "sources": sources,
            "needs_human": True,
            "reason": "Answer requires human verification"
        }

    excerpts = knowledge.get("answer", "Relevant support articles found.")
    return {
        "draft": (
            "Hello,\n\nThank you for contacting support. "
            "Here is the relevant information we found:\n\n"
            f"{excerpts}\n\n"
            "Please let us know if you need further assistance."
        ),
        "sources": sources,
        "needs_human": True,
        "reason": "Draft requires human approval before sending"
    }
