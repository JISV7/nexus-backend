from app.algorithms.dp_graph import solve_graph_routing
from app.network_routing.network_routing_schema import NetworkRoutingRequest, NetworkRoutingResponse

class NetworkRoutingService:
    @staticmethod
    def calculate_routing(request: NetworkRoutingRequest) -> NetworkRoutingResponse:
        result = solve_graph_routing(request.stages)
        return NetworkRoutingResponse(**result)
