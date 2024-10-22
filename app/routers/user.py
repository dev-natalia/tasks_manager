from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.schemas.user import UserSchema
from app.services.user import UserService
from app.utils.password import Password
from app.db.sqlalchemy_client import get_db

router = APIRouter(prefix="/user", tags=["user"])
user_service = UserService()
password = Password()


@router.post("/register")
def create_user(data: UserSchema, db: Session = Depends(get_db)):
    return user_service.create(data, db)
