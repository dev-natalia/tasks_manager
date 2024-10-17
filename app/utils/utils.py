from passlib.context import CryptContext

from app.models.user import UserModel


class Password:
    def __init__(self):
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password: str):
        return self.__pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.__pwd_context.verify(plain_password, hashed_password)

    def authenticate_user(self, user: UserModel, password: str):
        if not self.verify_password(password, user.hashed_password):
            return False
        return user
