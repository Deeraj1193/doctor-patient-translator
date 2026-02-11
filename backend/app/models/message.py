from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("sessions.id", ondelete="CASCADE"),
        nullable=False
    )

    role = Column(String, nullable=False)

    original_text = Column(Text, nullable=False)
    translated_text = Column(Text, nullable=False)

    source_language = Column(String, nullable=False)
    target_language = Column(String, nullable=False)

    audio_path = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship back to session
    session = relationship("Session", back_populates="messages")
