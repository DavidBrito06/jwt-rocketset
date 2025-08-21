import pytest
from .user_register_view import UserRegisterView
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse

class MockController:
    def registry(self, username: str, password: str) -> dict:
        return {"alguma": "coisa"}

def test_user_register_view():
    body = {
        "username": "Myusername",
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)
    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)

    print()
    print(response)
    print(response.body)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body == {'data': {'alguma': 'coisa'}}



def test_user_register_view_error():
    body = {
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)
    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)
