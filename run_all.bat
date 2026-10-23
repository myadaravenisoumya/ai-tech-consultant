@echo off
cd /d "%~dp0"
start "Knowledge Brain - 8000" cmd /k ".venv\Scripts\python.exe -m uvicorn main:app --app-dir task1-knowledge-brain --port 8000"
start "Inbox Agent - 8001" cmd /k ".venv\Scripts\python.exe -m uvicorn main:app --app-dir task2-inbox-agent --port 8001"
start "Meeting to Scope - 8002" cmd /k ".venv\Scripts\python.exe -m uvicorn main:app --app-dir task3-meeting-to-scope --port 8002"
