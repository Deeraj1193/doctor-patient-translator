@echo off
echo Starting Backend...
start cmd /k "cd backend && venv\Scripts\activate && uvicorn app.main:app --reload"

timeout /t 3 > nul

echo Starting Frontend...
start cmd /k "cd frontend && npm run dev"

timeout /t 5 > nul

echo Opening Web App...
start http://localhost:5173

echo All services launched.
