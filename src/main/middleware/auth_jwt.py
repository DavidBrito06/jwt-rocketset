from flask import request
from src.drivers.jwt_handler import JwtHandler
from src.errors.types.http_unauthorized import HttpUnauthorizedError

def auth_jwt_verify():
    jwt_handler = JwtHandler()
    raw_token = request.headers.get("Authorization")
    user_id = request.headers.get("uid")

    # Verifica se os headers existem
    if not raw_token or not user_id:
        raise HttpUnauthorizedError("Authorization token or user ID missing")

    # Divide o header e valida formato correto
    parts = raw_token.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HttpUnauthorizedError("Invalid Authorization header format")

    token = parts[1]

    # Decodifica token com try/except para evitar 500
    try:
        token_information = jwt_handler.decode_jwt_token(token)
    except Exception:
        raise HttpUnauthorizedError("Invalid or expired token")

    token_uid = token_information.get("user_id")
    if not token_uid:
        raise HttpUnauthorizedError("Token missing user_id")

    # Verifica se os IDs batem
    try:
        if int(token_uid) == int(user_id):
            return token_information
    except ValueError:
        raise HttpUnauthorizedError("Invalid user_id format")

    raise HttpUnauthorizedError("Invalid token or user ID mismatch")
