import uuid
from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.image import Image
    from app.models.like import Like
    from app.models.comment import Comment


class Post(SQLModel, table=True):
    __tablename__ = "posts"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    description: str
    user_id: uuid.UUID = Field(foreign_key="users.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: "User" = Relationship(back_populates="posts")
    images: List["Image"] = Relationship(back_populates="post")
    likes: List["Like"] = Relationship(back_populates="post")
    comments: List["Comment"] = Relationship(back_populates="post")
