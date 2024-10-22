import hashlib
from pydantic import BaseModel, field_validator


class UserSchema(BaseModel):
    username: str
    email: str
    password: str

    @field_validator("password")
    @classmethod
    def hash_password(cls, v: str) -> str:
        password_bytes = v.encode("utf-8")
        hash_obj = hashlib.sha256(password_bytes)
        hash_password = hash_obj.hexdigest()
        return hash_password

    class Config:
        orm_mode = True  # Permite compatibilidade com SQLAlchemy ORM
