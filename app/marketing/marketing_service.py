from app.algorithms.gradient_ascent import solve_marketing_optimization
from app.marketing.marketing_schema import MarketingOptimizationRequest, MarketingOptimizationResponse

class MarketingService:
    @staticmethod
    def optimize_marketing(request: MarketingOptimizationRequest) -> MarketingOptimizationResponse:
        # Convert Pydantic models to dictionaries for the algorithm
        channels = [c.model_dump() for c in request.channels]
        constraints = [c.model_dump() for c in request.constraints]
        
        result = solve_marketing_optimization(
            channels=channels,
            constraints=constraints
        )
        
        return MarketingOptimizationResponse(**result)
