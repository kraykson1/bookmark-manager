from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from app.database import engine, Base
from app import models
from app.routers import users as usersRout, bookmarks as bookmarksRout

app = FastAPI()

app.include_router(usersRout.router)
app.include_router(bookmarksRout.router)

Base.metadata.create_all(bind=engine)

@app.get("/healthz", include_in_schema=False)
def healthz():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception:
        raise HTTPException(status_code=503, detail="db-unavailable")