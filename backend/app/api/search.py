from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.message import Message

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("/")
def search_messages(query: str, db: Session = Depends(get_db)):
    results = db.query(Message).filter(
        Message.original_text.contains(query) |
        Message.translated_text.contains(query)
    ).all()

    return results
