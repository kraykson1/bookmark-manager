from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.models import Bookmark as BookmarkDB, User as UserDB
from app.schemas import BookmarkCreate, BookmarkResponse
from app.auth import get_current_user

router = APIRouter(prefix="/bookmarks", tags=["bookmarks"])

# получить все свои закладки
@router.get("/")
def get_bookmarks(db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    return db.query(BookmarkDB).filter(BookmarkDB.owner_id == current_user.id).all()

# создать новую закладку
@router.post("/", response_model=BookmarkResponse)
def create_bookmark(bookmark: BookmarkCreate, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    db_bookmark = BookmarkDB(
        url=bookmark.url,
        title=bookmark.title,
        description=bookmark.description,
        owner_id=current_user.id,
    )
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark

# найти свою закладку по её id
@router.get("/{bookmark_id}", response_model=BookmarkResponse)
def get_bookmark(bookmark_id: int, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    bookmark = db.query(BookmarkDB).filter(BookmarkDB.id == bookmark_id, BookmarkDB.owner_id == current_user.id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found.")
    return bookmark

# обновить свою закладку
@router.put("/{bookmark_id}", response_model=BookmarkResponse)
def put_bookmark(bookmark_id: int, bookmark_new: BookmarkCreate, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    bookmark = db.query(BookmarkDB).filter(BookmarkDB.id == bookmark_id, BookmarkDB.owner_id == current_user.id).first()
    if bookmark:
        bookmark.url = bookmark_new.url
        bookmark.title = bookmark_new.title
        bookmark.description = bookmark_new.description
        db.commit()
        return {"message": f"Bookmark updated."}
    raise HTTPException(status_code=404, detail="Bookmark not found.")

# удалить свою закладку
@router.delete("/{bookmark_id}")
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    bookmark = db.query(BookmarkDB).filter(BookmarkDB.id == bookmark_id, BookmarkDB.owner_id == current_user.id).first()
    if bookmark:
        db.delete(bookmark)
        return {"message": f"Bookmark deleted."}
    raise HTTPException(status_code=404, detail="Bookmark not found.")
