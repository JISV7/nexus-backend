from typing import Any, Dict, Optional

from pydantic import BaseModel


class ReportRequest(BaseModel):
    server_load_results: Optional[Dict[str, Any]] = None
    network_routing_results: Optional[Dict[str, Any]] = None
    marketing_optimization_results: Optional[Dict[str, Any]] = None
    ai_analysis: str


class ReportResponse(BaseModel):
    # This might not be used directly as we return a FileResponse
    status: str = "success"
