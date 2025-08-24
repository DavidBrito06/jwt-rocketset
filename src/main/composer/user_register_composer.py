from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repository.user_repository import UserRepository
from src.controllers.user_register import UserRegistrer
from src.view.user_register_view import UserRegisterView

def user_register_composer():
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)
    controller = UserRegistrer(model)
    view = UserRegisterView(controller)

    return view