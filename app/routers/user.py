from fastapi import APIRouter
from app.schemas.user import UserSchema
from app.crud.user import User
from app.utils.utils import Password

router = APIRouter(prefix="/user", tags=["user"])
user = User()
password = Password()


@router.post("/register")
def create_user(data: UserSchema):
    return user.create(data)
