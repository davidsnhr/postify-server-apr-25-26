

from datetime import datetime  # Import the class directly


from sqlmodel import SQLModel


class UserCreate(SQLModel):
    username: str
    name: str
    lastname: str
    email: str
    password: str
    
    
class UserRead(SQLModel):
    username: str
    name: str
    lastname: str
    email: str
    created_at: datetime