from pydantic import BaseModel, Field
from typing import List, Optional

class ChannelInput(BaseModel):
    name: str
    linear_coef: float = Field(..., description="The 'a' or 'b' coefficient (linear yield)")
    saturation_penalty: float = Field(..., description="The 'c' or 'd' coefficient (quadratic penalty for saturation)")

class ConstraintInput(BaseModel):
    type: str = Field(..., description="'sum_all' (budget) or 'individual' (channel specific)")
    target_channel: Optional[str] = Field(None, description="Required if type is 'individual'")
    operator: str = Field(..., description="'<=', '>=', or '=='")
    value: float

class MarketingOptimizationRequest(BaseModel):
    channels: List[ChannelInput]
    constraints: List[ConstraintInput]

class ChannelResult(BaseModel):
    name: str
    investment: float

class MarketingOptimizationResponse(BaseModel):
    max_value: float
    channels: List[ChannelResult]
