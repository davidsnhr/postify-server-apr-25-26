import uuid
from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.user import User


class Follower(SQLModel, table=True):
    __tablename__ = "followers"

    follower_id: uuid.UUID = Field(foreign_key="users.id", primary_key=True)
    following_id: uuid.UUID = Field(foreign_key="users.id", primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    follower_user: "User" = Relationship(
        back_populates="following",
        sa_relationship_kwargs={"foreign_keys": "[Follower.follower_id]"},
    )
    following_user: "User" = Relationship(
        back_populates="followers",
        sa_relationship_kwargs={"foreign_keys": "[Follower.following_id]"},
    )
