from fastapi import FastAPI, Depends, HTTPException, Response
from app.database import SessionLocal, engine, Base
from app.auth import router as auth_router
from sqlalchemy import text
from app import models
from app.routers import users as usersRout, bookmarks as bookmarksRout

app = FastAPI()

app.include_router(usersRout.router)
app.include_router(bookmarksRout.router)

Base.metadata.create_all(bind=engine)

@app.get("/healthz", include_in_schema=False)
def healthz():
    try:
        with engine.connect() as conn, text, Response:
            await conn.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception:
        raise HTTPException(status_code=503, detail="db-unavailable")