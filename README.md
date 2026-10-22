# AI Tech Consultant

A Python-based prototype containing three support automation services.

## Components

1. **Knowledge Brain** — collects support articles and retrieves relevant passages with source links.
2. **Inbox Agent** — drafts customer support responses and requires human approval.
3. **Meeting to Scope of Work** — structures meeting notes into requirements and flags estimates for human review.

## Requirements

- Python 3.10 or newer
- Packages: fastapi, uvicorn, httpx, beautifulsoup4, lxml, python-dotenv

## Setup

Create a virtual environment and install dependencies if needed:

    python -m venv .venv
    .venv\Scripts\python.exe -m pip install fastapi "uvicorn[standard]" httpx beautifulsoup4 lxml python-dotenv

## Run the services

Open three separate PowerShell windows from the project root.

Knowledge Brain:

    .\.venv\Scripts\python.exe -m uvicorn main:app --app-dir task1-knowledge-brain --port 8000

Inbox Agent:

    .\.venv\Scripts\python.exe -m uvicorn main:app --app-dir task2-inbox-agent --port 8001

Meeting to Scope of Work:

    .\.venv\Scripts\python.exe -m uvicorn main:app --app-dir task3-meeting-to-scope --port 8002

## API documentation

- Knowledge Brain: http://127.0.0.1:8000/docs
- Inbox Agent: http://127.0.0.1:8001/docs
- Meeting to Scope of Work: http://127.0.0.1:8002/docs

## Limitations

This is an early prototype. Retrieval currently uses basic keyword matching, the article collection is limited to a small sample, and response generation is template-based rather than Claude-powered. Estimates and customer replies require human review. Automated evaluations, incremental updates, and full assignment acceptance tests remain to be completed.

No real customer email is sent by these services.
