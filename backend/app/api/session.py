from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.session import Session as SessionModel
from app.schemas.session_schema import SessionResponse

router = APIRouter(prefix="/sessions", tags=["Sessions"])


@router.post("/", response_model=SessionResponse)
def create_session(db: Session = Depends(get_db)):
    new_session = SessionModel()
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session
