# System Design — AI Tech Consultant

## 1. Overview

The project contains three independent Python FastAPI services for support knowledge retrieval, email drafting, and meeting-to-scope generation.

## 2. Architecture

### Task 1: Knowledge Brain
- Source: Brilliant Directories Support Center sitemap.
- Collection: Python HTTP client and HTML parser.
- Storage: Local JSON article collection.
- Retrieval: Keyword matching against article content.
- API: POST /query returns matching excerpts, source URLs, and a human-escalation flag.
- Current limitation: Only five sample pages are collected; semantic search, embeddings, Claude-generated answers, and scheduled incremental updates are not implemented.

### Task 2: Inbox Agent
- Input: Email subject and body.
- Dependency: Calls the Knowledge Brain API.
- Output: Draft response, sources, and human-review status.
- Safety: Does not send emails automatically.
- Current limitation: Drafting uses templates and retrieved excerpts, not Claude.

### Task 3: Meeting to Scope of Work
- Input: Client name, meeting transcript, and optional previous scope.
- Dependency: Calls the Knowledge Brain API for relevant support references.
- Output: Structured meeting requirements, deliverables, estimate status, and approval status.
- Safety: Estimates are not invented; human approval is required.
- Current limitation: Requirement extraction and scope comparison are basic and do not use an LLM.

## 3. API Endpoints

| Service | Endpoint | Purpose |
|---|---|---|
| Knowledge Brain | GET /health | Health check |
| Knowledge Brain | POST /query | Retrieve support references |
| Inbox Agent | GET /health | Health check |
| Inbox Agent | POST /draft | Draft a support response |
| Meeting to Scope | GET /health | Health check |
| Meeting to Scope | POST /generate-sow | Structure meeting notes |

Interactive API documentation is available at `/docs` on each service's local port.

## 4. Data Flow

1. The collector downloads support pages and saves extracted content to JSON.
2. The Knowledge Brain searches the local collection and returns source references.
3. The Inbox Agent uses those references when preparing a draft.
4. The meeting service queries the Knowledge Brain and structures the provided notes.
5. Human review remains necessary before customer communication or scope approval.

## 5. Safety and Failure Handling

- Source URLs are returned when available.
- The Inbox Agent flags drafts for human review.
- If the Knowledge Brain is unavailable, the Inbox Agent returns a safe fallback and flags human review.
- Scope estimates remain explicitly unverified.
- Services do not send customer emails or approve proposals automatically.

## 6. Limitations and Next Steps

1. Collect and validate the full set of relevant support articles.
2. Add incremental collection and deduplication.
3. Implement semantic retrieval and Claude API integration when credentials are available.
4. Add the required human feedback workflow and safe handling of repeated unchanged drafts.
5. Improve structured requirement extraction and scope-change comparisons.
6. Build automated evaluation suites with at least 20 test cases per task.
7. Measure latency and cost using actual runs before reporting metrics.
8. Test service failures, unsupported questions, and conflicting requirements.

## 7. Design Decision

Python and FastAPI were used across the prototype to reduce setup complexity and provide simple HTTP APIs. Local JSON storage keeps the prototype easy to inspect, but it is not suitable for a large production knowledge base without additional indexing and update controls.
