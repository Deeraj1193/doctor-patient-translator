from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.message import Message
from app.services.ai_service import summarize_conversation

router = APIRouter(prefix="/summary", tags=["Summary"])


@router.post("/{session_id}")
def generate_summary(session_id: int, db: Session = Depends(get_db)):

    messages = db.query(Message).filter(Message.session_id == session_id).all()

    if not messages:
        raise HTTPException(status_code=404, detail="No messages found")

    conversation_text = "\n".join(
        [f"{msg.role}: {msg.original_text}" for msg in messages]
    )

    summary = summarize_conversation(conversation_text)

    return {"summary": summary}
