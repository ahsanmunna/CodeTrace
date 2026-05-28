from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
import secrets
import json

from fastapi.responses import FileResponse
from database import get_db
from models import User, Request, Feedback
from log_parser import parse_log
from classifier import classify
from rate_limiter import is_rate_limited
from response_engine import (
    calculate_severity,
    estimate_debug_time,
    get_fix_suggestion
)

app = FastAPI()


# -------------------
# Schemas
# -------------------
class RegisterRequest(BaseModel):
    email: EmailStr


class AnalyzeRequest(BaseModel):
    api_key: str
    log: str


class FeedbackRequest(BaseModel):
    api_key: str
    request_id: int
    is_correct: bool
    comment: str | None = None


# -------------------
# Register Endpoint
# -------------------
@app.post("/register")
def register_user(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    # Check if user already exists
    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Generate API key
    api_key = secrets.token_urlsafe(32)

    # Create user
    new_user = User(
        email=request.email,
        api_key=api_key,
        tier="free"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "api_key": api_key
    }


# -------------------
# Analyze Endpoint
# -------------------
@app.post("/analyze")
def analyze_log(
    request: AnalyzeRequest,
    db: Session = Depends(get_db)
):
    # Validate API key
    user = db.query(User).filter(
        User.api_key == request.api_key
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    # Rate limit check
    if is_rate_limited(request.api_key):
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Free tier allows 10 requests per minute."
        )

    # Parse log
    parsed = parse_log(request.log)

    # Extract error text safely
    error_text = parsed.get("error") or parsed.get("message") or request.log

    # Classify error
    classification = classify(error_text)
    category = classification["category"]

    # Severity
    severity = calculate_severity(category)

    # Estimated fix time
    estimated_time = estimate_debug_time(category, severity)

    # Fix suggestion
    fix_suggestion = get_fix_suggestion(category, parsed.get("error_type"))

    # Build response
    response_data = {
        "parsed_log": parsed,
        "classification": classification,
        "severity": severity,
        "estimated_fix_time_minutes": estimated_time,
        "fix_suggestion": fix_suggestion
    }

    # Save request
    new_request = Request(
        user_id=user.id,
        endpoint="/analyze",
        input_data=request.log,
        response_data=json.dumps(response_data),
        status="success"
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    # Return response
    return {
        "status": "success",
        "data": response_data,
        "request_id": new_request.id
    }


# -------------------
# Feedback Endpoint
# -------------------
@app.post("/feedback")
def submit_feedback(
    request: FeedbackRequest,
    db: Session = Depends(get_db)
):
    # Validate API key
    user = db.query(User).filter(
        User.api_key == request.api_key
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    # Validate request exists
    existing_request = db.query(Request).filter(
        Request.id == request.request_id,
        Request.user_id == user.id
    ).first()

    if not existing_request:
        raise HTTPException(
            status_code=404,
            detail="Request not found"
        )

    # Save feedback
    feedback = Feedback(
        user_id=user.id,
        request_id=request.request_id,
        is_correct=request.is_correct,
        comment=request.comment
    )

    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    return {
        "status": "success",
        "message": "Feedback submitted successfully",
        "feedback_id": feedback.id
    }

@app.get("/")
def landing():
    return FileResponse("index.html")