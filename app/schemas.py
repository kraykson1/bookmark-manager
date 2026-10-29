from models import User as UserDB, Bookmark as BookmarkDB, Tag as TagDB
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int 
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class BookmarkCreate(BaseModel):
    url: str
    title: str 
    description: str | None = None

class BookmarkResponse(BaseModel):
    id: int 
    url: str 
    title: str
    description: str | None = None
    owner_id: int

class TagResponse(BaseModel):
    id: int
    name: str