from sqlalchemy.orm import Session
from app.models.user import UserModel
from app.schemas.user import UserSchema


class User:
    def __init__(self):
        pass

    def create(self, db_session: Session, data: UserSchema):
        db_user = UserModel(
            username=data.username,
            email=data.email,
            hashed_password=data.password,
        )
        db_session.add(db_user)
        db_session.commit()
        db_session.refresh(db_user)
        return db_user
