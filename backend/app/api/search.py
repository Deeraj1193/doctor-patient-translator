from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.message import Message
from typing import List

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
def search_messages(
    query: str = Query(...),
    session_id: int = Query(...),
    db: Session = Depends(get_db)
):
    results = db.query(Message).filter(
        Message.session_id == session_id,
        Message.original_text.contains(query)
    ).all()

    return results
