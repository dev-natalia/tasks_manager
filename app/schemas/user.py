from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    hashed_password: Optional[str] = None

    class Config:
        orm_mode = True  # Permite compatibilidade com SQLAlchemy ORM
