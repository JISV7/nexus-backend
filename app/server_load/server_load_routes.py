from fastapi import APIRouter

from app.server_load.server_load_controller import ServerLoadController
from app.server_load.server_load_schema import ServerLoadRequest, ServerLoadResponse

router = APIRouter(prefix="/server-load", tags=["Server Load"])


@router.post("/optimize", response_model=ServerLoadResponse)
async def optimize_server_load(request: ServerLoadRequest):
    return ServerLoadController.calculate_optimization(request)
