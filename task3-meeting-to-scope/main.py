from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import httpx

app = FastAPI(title="Meeting to Scope of Work")

KNOWLEDGE_API = "http://127.0.0.1:8000/query"

class Meeting(BaseModel):
    client: str = "New Client"
    transcript: str
    previous_scope: str = ""

@app.get("/health")
def health():
    return {"status": "healthy", "agent": "Meeting to Scope of Work"}

@app.post("/generate-sow")
def generate_sow(meeting: Meeting):
    transcript = meeting.transcript.strip()
    if not transcript:
        return {"error": "Meeting transcript is required"}

    try:
        response = httpx.post(
            KNOWLEDGE_API,
            json={"question": transcript},
            timeout=15
        )
        response.raise_for_status()
        knowledge = response.json()
    except Exception:
        knowledge = {"sources": [], "needs_human": True}

    lines = [line.strip(" -\t") for line in transcript.splitlines()
             if line.strip()]

    scope = {
        "client": meeting.client,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "meeting_requirements": lines,
        "deliverables": lines,
        "assumptions": ["Requirements are based only on the supplied meeting notes."],
        "estimate": {
            "status": "Needs human estimation",
            "hours": None,
            "reason": "No verified effort estimates were supplied."
        },
        "knowledge_sources": knowledge.get("sources", []),
        "scope_changes": [],
        "approval_status": "Pending human approval"
    }

    if meeting.previous_scope:
        scope["scope_changes"] = [
            "A previous scope was supplied. Compare the old and new requirements before approving."
        ]
        scope["previous_scope"] = meeting.previous_scope

    return scope
