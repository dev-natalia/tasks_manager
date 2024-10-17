from sqlalchemy.orm import Session
from app.models.user import UserModel
from app.schemas.user import UserSchema


class User:
    def __init__(self):
        pass

    def create(self, db_session: Session, data: UserSchema):
        # TODO: ADICIONAR CRIAÇÃO DE HASH COMO CONFIG DE USERSCHEMA
        db_user = UserModel(
            username=data.username,
            email=data.email,
            hashed_password=data.hashed_password,
        )
        db_session.add(db_user)
        db_session.commit()
        db_session.refresh(db_user)
        # TODO: ADICIONAR EXCEPTION PARA CASO USERNAME JÁ EXISTA

        return db_user
