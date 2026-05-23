from typing import Dict, List

from pydantic import BaseModel


class NetworkRoutingRequest(BaseModel):
    # List of stages, e.g., [{"A": {"B": 4, "C": 6, "D": 3}}, ...]
    stages: List[Dict[str, Dict[str, int]]]


class NetworkRoutingResponse(BaseModel):
    min_latency: int
    path: List[str]
