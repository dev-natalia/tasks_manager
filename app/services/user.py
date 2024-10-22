from sqlalchemy.orm import Session
from app.schemas.user import UserSchema
from app.utils.password import Password
from app.crud.user import UserCRUD


class UserService:
    def __init__(self):
        self.password = Password()
        self.user_crud = UserCRUD()

    def create(self, data: UserSchema, db: Session):
        check_user = self.user_crud.get_by_username(db, data)
        if check_user:
            return "Username já cadastrado. Por favor, escolha outro."

        data.hashed_password = self.password.get_password_hash(data.password)
        user = self.user_crud.create(db, data)
        return user

    def update(self, data: UserSchema, db: Session):
        data.hashed_password = self.password.get_password_hash(data.password)
        user = self.user_crud.get_by_username(db, data)
        if user:
            self.user_crud.update(db, data, user)
            return user
        else:
            return "Username não cadastrado. Crie uma nova conta."

    def delete(self, data: UserSchema, db: Session):
        user = self.user_crud.get_by_username(db, data)
        if user:
            self.user_crud.delete(db, data, user)
            return "User deletado com sucesso."
        else:
            return "Username não cadastrado. Crie uma nova conta."
