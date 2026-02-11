from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.message import Message as MessageModel
from app.models.session import Session as SessionModel
from app.schemas.message_schema import MessageCreate, MessageResponse
from app.services.ai_service import translate_text

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.post("/", response_model=MessageResponse)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):

    session = db.query(SessionModel).filter(SessionModel.id == message.session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    translated_text = translate_text(
        message.original_text,
        message.source_language,
        message.target_language,
    )

    new_message = MessageModel(
        session_id=message.session_id,
        role=message.role,
        original_text=message.original_text,
        translated_text=translated_text,
        source_language=message.source_language,
        target_language=message.target_language,
    )

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message
