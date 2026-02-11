from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.message import Message
from app.services.ai_service import generate_summary_text

router = APIRouter()

@router.get("/summary/{session_id}")
def generate_summary(session_id: int, db: Session = Depends(get_db)):
    messages = (
        db.query(Message)
        .filter(Message.session_id == session_id)
        .order_by(Message.created_at.asc())
        .all()
    )

    conversation_text = "\n".join(
        [f"{m.role}: {m.original_text}" for m in messages]
    )

    summary = generate_summary_text(conversation_text)

    return {"summary": summary}
