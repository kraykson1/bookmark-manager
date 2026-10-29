from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

# Связь многие-ко-многим между закладками и тегами
bookmark_tag = Table(
    "bookmark_tag",
    Base.metadata,
    Column("bookmark_id", Integer, ForeignKey("bookmarks.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    bookmarks = relationship("Bookmark", back_populates="owner", cascade="all, delete-orphan")

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="bookmarks")
    tags = relationship("Tag", secondary=bookmark_tag, back_populates="bookmarks")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    bookmarks = relationship("Bookmark", secondary=bookmark_tag, back_populates="tags")