from app.server_load.server_load_schema import ServerLoadRequest, ServerLoadResponse
from app.server_load.server_load_service import ServerLoadService


class ServerLoadController:
    @staticmethod
    def calculate_optimization(request: ServerLoadRequest) -> ServerLoadResponse:
        return ServerLoadService.optimize_load(request)
