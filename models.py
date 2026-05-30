from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
import datetime

from database import Base


# -------------------
# Users Table
# -------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    api_key = Column(String, unique=True, nullable=False)
    tier = Column(String, nullable=False, default="free")
    created_at = Column(DateTime, server_default=func.now())

    requests = relationship("Request", back_populates="user")
    feedback = relationship("Feedback", back_populates="user")


# -------------------
# Requests Table
# -------------------
class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    endpoint = Column(String, nullable=False)
    input_data = Column(Text, nullable=False)
    response_data = Column(Text, nullable=True)

    status = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="requests")
    feedback = relationship("Feedback", back_populates="request")


# -------------------
# Error Patterns Table
# -------------------
class ErrorPattern(Base):
    __tablename__ = "error_patterns"

    id = Column(Integer, primary_key=True, index=True)

    error_type = Column(String, nullable=False)
    pattern = Column(Text, nullable=False)
    fix_suggestion = Column(Text, nullable=False)

    severity = Column(String, nullable=False)
    frequency = Column(Integer, default=0)
    doc_url = Column(String, nullable=True)

    created_at = Column(DateTime, server_default=func.now())


# -------------------
# Feedback Table
# -------------------
class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    request_id = Column(Integer, ForeignKey("requests.id"), nullable=False)

    is_correct = Column(Boolean, nullable=False)
    comment = Column(Text, nullable=True)

    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="feedback")
    request = relationship("Request", back_populates="feedback")