import uuid
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.post import Post


class Comment(SQLModel, table=True):
    __tablename__ = "comments"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    content: str
    user_id: uuid.UUID = Field(foreign_key="users.id")
    post_id: uuid.UUID = Field(foreign_key="posts.id")
    parent_id: Optional[uuid.UUID] = Field(default=None, foreign_key="comments.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: "User" = Relationship(back_populates="comments")
    post: "Post" = Relationship(back_populates="comments")
    replies: List["Comment"] = Relationship(
        back_populates="parent",
        sa_relationship_kwargs={"foreign_keys": "[Comment.parent_id]"},
    )
    parent: Optional["Comment"] = Relationship(
        back_populates="replies",
        sa_relationship_kwargs={
            "foreign_keys": "[Comment.parent_id]",
            "remote_side": "[Comment.id]",
        },
    )
