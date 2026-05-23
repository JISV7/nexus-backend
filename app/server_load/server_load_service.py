from app.algorithms.dp_knapsack import solve_knapsack
from app.server_load.server_load_schema import ServerLoadRequest, ServerLoadResponse


class ServerLoadService:
    @staticmethod
    def optimize_load(request: ServerLoadRequest) -> ServerLoadResponse:
        weights = [ms.ram_requirement for ms in request.microservices]
        values = [ms.priority_value for ms in request.microservices]
        names = [ms.name for ms in request.microservices]

        result = solve_knapsack(request.max_capacity, weights, values, names)

        return ServerLoadResponse(**result)
