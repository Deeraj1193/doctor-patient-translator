from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to messages
    messages = relationship(
        "Message",
        back_populates="session",
        cascade="all, delete-orphan"
    )
