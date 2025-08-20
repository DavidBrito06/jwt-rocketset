from src.models.interface.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler

class UserRegistrer:
    def __init__(self, user_repository: UserRepositoryInterface)->None:
        self.__user_repository = user_repository
        self.__password_handle = PasswordHandler()

    def registry(self, username: str, password: str) -> dict:
        hashed_password = self.__create_hash_passowrd(password)
        self.__register_new_user(username, hashed_password)
        return self.__format_response(username)

    def __create_hash_passowrd(self, password: str) -> str:
        hashed_password = self.__password_handle.encrypt_password(password)
        return hashed_password
    
    def __register_new_user(self, username: str, hashed_passowrd)-> None:
        self.__user_repository.registry_user(username, hashed_passowrd)
    
    def __format_response(self, username: str)-> dict:
        return {
            "type": "User",
            "count": 1,
            "username": username
        }

