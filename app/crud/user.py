from sqlalchemy.orm import Session
from app.models.user import UserModel
from app.schemas.user import UserSchema


class UserCRUD:
    def __init__(self):
        pass

    def create(self, db: Session, data: UserSchema):
        user = UserModel(
            username=data.username,
            hashed_password=data.hashed_password,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_by_username(self, db: Session, data: UserSchema):
        user = db.query(UserModel).filter(UserModel.username == data.username).first()
        return user

    def update(self, db: Session, data: UserSchema, user: UserModel):
        user.username = data.username
        user.hashed_password = data.hashed_password
        db.commit()
        db.refresh(user)

    def delete(self, db: Session, data: UserSchema, user: UserModel):
        db.query(UserModel).filter(UserModel.username == data.username).delete(
            synchronize_session=False
        )
        db.commit()
