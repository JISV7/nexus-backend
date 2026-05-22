from pydantic import BaseModel

class MarketingOptimizationRequest(BaseModel):
    budget: float = 10.0
    # f(x1, x2) = a*x1 + b*x2 - c*x1^2 - d*x2^2 + e*x1*x2 + f
    a: float = 4.0
    b: float = 5.0
    c: float = 0.2
    d: float = 0.3
    e: float = 0.0
    f: float = 0.0

class MarketingOptimizationResponse(BaseModel):
    x1: float
    x2: float
    max_value: float
