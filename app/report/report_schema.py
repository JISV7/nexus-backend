from pydantic import BaseModel
from typing import Any, Dict

class ReportRequest(BaseModel):
    server_load_results: Dict[str, Any]
    network_routing_results: Dict[str, Any]
    marketing_optimization_results: Dict[str, Any]
    ai_analysis: str

class ReportResponse(BaseModel):
    # This might not be used directly as we return a FileResponse
    status: str = "success"
