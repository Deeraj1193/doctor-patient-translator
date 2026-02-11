from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MessageBase(BaseModel):
    session_id: int
    role: str
    original_text: Optional[str] = None
    source_language: Optional[str] = None
    target_language: Optional[str] = None
    audio_path: Optional[str] = None


class MessageCreate(MessageBase):
    pass


class MessageResponse(MessageBase):
    id: int
    translated_text: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
