from app.algorithms.gradient_ascent import solve_marketing_optimization, create_quadratic_model
from app.marketing.marketing_schema import MarketingOptimizationRequest, MarketingOptimizationResponse

class MarketingService:
    @staticmethod
    def optimize_marketing(request: MarketingOptimizationRequest) -> MarketingOptimizationResponse:
        func, grad = create_quadratic_model(
            request.a, request.b, request.c, request.d, request.e, request.f
        )
        
        result = solve_marketing_optimization(
            func=func,
            grad_func=grad,
            budget=request.budget
        )
        
        return MarketingOptimizationResponse(**result)
