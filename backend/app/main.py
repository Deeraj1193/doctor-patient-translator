from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import session, message
from app.api import session as session_router
from app.api import message as message_router
from app.api import search as search_router
from app.api import summary as summary_router

app = FastAPI(title="Doctor-Patient Translator API")

Base.metadata.create_all(bind=engine)

app.include_router(session_router.router)
app.include_router(message_router.router)
app.include_router(search_router.router)
app.include_router(summary_router.router)


@app.get("/")
def root():
    return {"message": "Doctor-Patient Translator API Running"}
