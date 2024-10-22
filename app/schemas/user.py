from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    password: Optional[str]
    hashed_password: Optional[str]

    class Config:
        orm_mode = True  # Permite compatibilidade com SQLAlchemy ORM
