from typing import Any, Dict

from pydantic import BaseModel


class AIAnalysisRequest(BaseModel):
    server_load_results: Dict[str, Any]
    network_routing_results: Dict[str, Any]
    marketing_optimization_results: Dict[str, Any]


class AIAnalysisResponse(BaseModel):
    analysis: str
