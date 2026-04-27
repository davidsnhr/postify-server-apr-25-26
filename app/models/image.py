import uuid
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.post import Post


class Image(SQLModel, table=True):
    __tablename__ = "images"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    url: str
    order: int = Field(default=0)
    post_id: uuid.UUID = Field(foreign_key="posts.id")

    post: "Post" = Relationship(back_populates="images")
