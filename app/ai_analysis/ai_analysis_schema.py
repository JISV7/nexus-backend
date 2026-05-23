from typing import Any, Dict, Optional

from pydantic import BaseModel


class AIAnalysisRequest(BaseModel):
    server_load_results: Optional[Dict[str, Any]] = None
    network_routing_results: Optional[Dict[str, Any]] = None
    marketing_optimization_results: Optional[Dict[str, Any]] = None


class AIAnalysisResponse(BaseModel):
    analysis: str
