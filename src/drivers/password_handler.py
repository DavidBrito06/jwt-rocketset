import bcrypt

class PasswordHandler:
    def encrypt_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def check_password(self, password: str, hashed_password: bytes) -> bool:
        # corrigido aqui: encode() em vez de ()
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)


