from .user_register import UserRegistrer

class MockUserRepository:
    def __init__(self):
        self.registry_user_attibutes = {}

    def registry_user(self, username, password) -> None:
        self.registry_user_attibutes["username"] = username
        self.registry_user_attibutes["password"] = password


def test_registry():
    repository = MockUserRepository()
    controller = UserRegistrer(repository)

    username = "olaMundo"
    password = "MinhaSenha"

    response = controller.registry(username, password)
    
    assert response["type"] == "User"
    assert response["username"] == username

    assert repository.registry_user_attibutes["username"] == username
    assert repository.registry_user_attibutes["password"] is not None
    assert repository.registry_user_attibutes["password"] != password
