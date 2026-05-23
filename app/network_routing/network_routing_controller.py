from app.network_routing.network_routing_schema import (
    NetworkRoutingRequest,
    NetworkRoutingResponse,
)
from app.network_routing.network_routing_service import NetworkRoutingService


class NetworkRoutingController:
    @staticmethod
    def find_shortest_path(request: NetworkRoutingRequest) -> NetworkRoutingResponse:
        return NetworkRoutingService.calculate_routing(request)
