# CodeTrace — Error Intelligence API

CodeTrace is a backend API service that accepts raw error logs and stack traces and returns structured, machine-readable debugging intelligence as JSON. It is not a chatbot — it is a developer tool designed to be plugged into pipelines.

## Live API

Base URL: `codetrace-production-1a79.up.railway.app`

API Docs: `codetrace-production-1a79.up.railway.app/docs`

## How it works

1. Developer sends a POST request with their raw error log and API key
2. Parser extracts file name, line number, error type, and message
3. ML classifier categorizes the error and returns a confidence score
4. Response engine scores severity, estimates debug time, and returns fix suggestions as structured JSON

## Quick start

```bash
# 1. Register and get your API key
curl -X POST https://codetrace-production-6a5d.up.railway.app/register \
  -H "Content-Type: application/json" \
  -d '{"email": "you@example.com"}'

# 2. Analyze an error log
curl -X POST https://codetrace-production-6a5d.up.railway.app/analyze \
  -H "Content-Type: application/json" \
  -d '{"api_key": "your_key", "log": "ZeroDivisionError: division by zero"}'
```

## Example response

```json
{
  "status": "success",
  "data": {
    "parsed_log": {
      "error_type": "ZeroDivisionError",
      "file": "app.py",
      "line": 42,
      "message": "division by zero"
    },
    "classification": {
      "category": "runtime_error",
      "confidence": 0.87
    },
    "severity": 6,
    "estimated_fix_time_minutes": 35,
    "fix_suggestion": "Inspect stack trace and handle edge cases or invalid inputs."
  },
  "request_id": 1
}
```

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Create account and receive API key |
| POST | `/analyze` | Send error log, receive structured diagnostic JSON |
| POST | `/feedback` | Flag wrong classifications to retrain the model |

## Features

- Multi-language log parsing — Python, Java, Node.js
- ML error classification with confidence scoring via `predict_proba()`
- Severity scoring (0–10) and estimated debug time
- Fix suggestions mapped to error categories
- API key authentication
- Rate limiting — 10 requests per minute on free tier
- Feedback loop — user flags retrain the classifier over time
- Cross-user pattern frequency intelligence

## Tech stack

| Layer | Tool |
|---|---|
| Backend | FastAPI |
| Database | PostgreSQL |
| Caching / Rate Limiting | Redis |
| ML Classification | scikit-learn |
| Containerization | Docker |
| Deployment | Railway |

## Why not just use AI?

AI gives you a prose paragraph. CodeTrace gives machine-readable JSON. A script can read JSON and automatically create a Jira ticket, fire a Slack alert, tag severity, and update a dashboard — zero human in the loop. Nobody can automate a paragraph.