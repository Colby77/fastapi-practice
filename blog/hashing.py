from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        hashed_password = password_context.hash(password)
        return hashed_password

    def verify(hashed_password, plain_password):
        return password_context.verify(plain_password, hashed_password)