import uuid
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship



class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(unique=True, index=True)
    name: str
    lastname: str
    email: str = Field(unique=True, index=True)
    password: str
    created_at: datetime
    
    posts: List['Post'] = Relationship(back_populates='user')
    
    