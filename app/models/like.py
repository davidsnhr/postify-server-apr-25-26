import uuid
from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.post import Post


class Like(SQLModel, table=True):
    __tablename__ = "likes"

    user_id: uuid.UUID = Field(foreign_key="users.id", primary_key=True)
    post_id: uuid.UUID = Field(foreign_key="posts.id", primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: "User" = Relationship(back_populates="likes")
    post: "Post" = Relationship(back_populates="likes")
