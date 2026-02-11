from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MessageCreate(BaseModel):
    session_id: int
    role: str
    original_text: str
    source_language: str
    target_language: str


class MessageResponse(BaseModel):
    id: int
    session_id: int
    role: str
    original_text: str
    translated_text: str
    source_language: str
    target_language: str
    audio_path: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
