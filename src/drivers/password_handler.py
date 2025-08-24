import bcrypt

class PasswordHandler:
    def encrypt_password(self, password: str) -> str:
        """Gera um hash da senha e retorna como string para salvar no banco."""
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password: str, hashed_password: str) -> bool:
        """Compara a senha com o hash armazenado (string)."""
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))



