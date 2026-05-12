



from datetime import datetime
import uuid

from sqlmodel import SQLModel


class PostCreate(SQLModel):
    description: str
    user_id: uuid.UUID
    
    
class PostRead(SQLModel):
    id: uuid.UUID
    description: str
    user_id: uuid.UUID
    created_at: datetime