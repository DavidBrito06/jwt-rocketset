import jwt
from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_info

class JwtHandler:
    def create_jwt_token(self, body: dict) -> str:
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(hours=int(jwt_info["JWT_HOURS"])),
                **body
            },
            key=jwt_info["KEY"],
            algorithm=jwt_info["ALGORITHM"]
        )
        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(
            token,
            key=jwt_info["KEY"],
            algorithms=[jwt_info["ALGORITHM"]]  # Linha corrigida
        )
        return token_information
    