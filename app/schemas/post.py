import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel


class PostCreate(SQLModel):
    description: str
    user_id: uuid.UUID


class PostRead(SQLModel):
    id: uuid.UUID
    description: str
    user_id: uuid.UUID
    created_at: datetime


class PostUpdate(SQLModel):
    description: Optional[str] = None
