import uuid
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.post import Post
    from app.models.like import Like
    from app.models.comment import Comment
    from app.models.follower import Follower


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(unique=True, index=True)
    name: str
    lastname: str
    email: str = Field(unique=True, index=True)
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    posts: List["Post"] = Relationship(back_populates="user")
    likes: List["Like"] = Relationship(back_populates="user")
    comments: List["Comment"] = Relationship(back_populates="user")
    following: List["Follower"] = Relationship(
        back_populates="follower_user",
        sa_relationship_kwargs={"foreign_keys": "[Follower.follower_id]"},
    )
    followers: List["Follower"] = Relationship(
        back_populates="following_user",
        sa_relationship_kwargs={"foreign_keys": "[Follower.following_id]"},
    )
