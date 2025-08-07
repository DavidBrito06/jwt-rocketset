from .user_repository import UserRepository
from unittest.mock import Mock

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self):
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_repository():
    username = "David"
    password = "test"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value
    print(cursor)
    print(cursor.execute.call_args[0])

