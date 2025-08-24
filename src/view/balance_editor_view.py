from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from src.errors.types.http_bad_request import HttpBadRequestError

class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterface)-> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get("new_balance")
        # O user_id deve ser obtido da URL, não do corpo da requisição PATCH,
        # pois a URL é /bank/balance/{user_id}.
        user_id = http_request.params.get("user_id")
        header_user_id = http_request.headers.get("uid")

        self.__validate_input(new_balance, user_id, header_user_id)
        
        # Converte o new_balance para float antes de passar para o controller.
        # Isso garante que a requisição com o valor como string (ex: "150.00")
        # será tratada corretamente.
        new_balance_float = float(new_balance)
        
        response = self.__controller.edit(user_id, new_balance_float)

        return HttpResponse(body={"data": response}, status_code=200)

    def __validate_input(self, new_balance: any, user_id: any, header_user_id: any) -> None:
        if (
            not new_balance
            or not user_id
            or int(header_user_id) != int(user_id)
        ):
            raise HttpBadRequestError("Invalid input")

        # Tenta converter o new_balance para float e trata a exceção
        # se a conversão não for possível (ex: se for uma string como "abc").
        try:
            float(new_balance)
        except (ValueError, TypeError):
            raise HttpBadRequestError("Invalid input: new_balance must be a number")

        
        