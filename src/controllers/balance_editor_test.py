from .balance_editor import BalanceEditor

class MockUserEditor:
    def __init__(self):
        self.edited_data = {}
    
    # precisa ter o mesmo nome da interface real!
    def edit_balance(self, user_id, new_balance):
        self.edited_data["user_id"] = user_id
        self.edited_data["new_balance"] = new_balance


def test_balance_editor():
    user_id = 1
    new_balance = 200.00

    # instanciando corretamente o mock
    mock_user_editor = MockUserEditor()
    editor_balance = BalanceEditor(mock_user_editor)

    response = editor_balance.edit(user_id, new_balance)

    # Asserts do retorno
    assert response["type"] == "User"
    assert response["Count"] == 1
    assert response["new_balance"] == new_balance

    # Asserts do mock (garante que o método foi chamado com os dados certos)
    assert mock_user_editor.edited_data["user_id"] == user_id
    assert mock_user_editor.edited_data["new_balance"] == new_balance
