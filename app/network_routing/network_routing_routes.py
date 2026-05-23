from fastapi import APIRouter

from app.network_routing.network_routing_controller import NetworkRoutingController
from app.network_routing.network_routing_schema import (
    NetworkRoutingRequest,
    NetworkRoutingResponse,
)

router = APIRouter(prefix="/network-routing", tags=["Network Routing"])


@router.post("/optimize", response_model=NetworkRoutingResponse)
async def optimize_network_routing(request: NetworkRoutingRequest):
    return NetworkRoutingController.find_shortest_path(request)
