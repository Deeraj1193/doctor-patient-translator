import os
import uuid
from uuid import uuid4
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.message import Message
from app.schemas.message_schema import MessageCreate, MessageResponse
from app.services.ai_service import translate_text
from typing import List

router = APIRouter(prefix="/messages", tags=["Messages"])

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@router.post("/", response_model=MessageResponse)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):

    translated_text = None
    if message.original_text:
        translated_text = translate_text(
            message.original_text,
            message.source_language,
            message.target_language,
        )

    db_message = Message(
        session_id=message.session_id,
        role=message.role,
        original_text=message.original_text,
        translated_text=translated_text,
        source_language=message.source_language,
        target_language=message.target_language,
        audio_path=message.audio_path
    )

    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message

@router.get("/{session_id}", response_model=List[MessageResponse])
def get_messages(session_id: int, db: Session = Depends(get_db)):
    return db.query(Message).filter(Message.session_id == session_id).all()

@router.post("/audio")
async def upload_audio(
    session_id: int = Form(...),
    role: str = Form(...),
    source_language: str = Form(...),
    target_language: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_ext}"
    filepath = os.path.join(upload_dir, filename)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    new_message = Message(
        session_id=session_id,
        role=role,
        original_text="Voice message",
        translated_text="Voice message",
        source_language=source_language,
        target_language=target_language,
        audio_path=f"uploads/{filename}",
    )

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message