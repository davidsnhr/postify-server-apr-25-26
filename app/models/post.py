import uuid
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship



class Post(SQLModel, table=True):
    __tablename__="posts"
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    description: str
    user_id: uuid.UUID = Field(foreign_key="users.id")
    create_at: datetime
    
    user: "User" = Relationship(back_populates="posts")