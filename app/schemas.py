from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

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