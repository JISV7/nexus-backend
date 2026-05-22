from app.marketing.marketing_service import MarketingService
from app.marketing.marketing_schema import MarketingOptimizationRequest, MarketingOptimizationResponse

class MarketingController:
    @staticmethod
    def calculate_marketing_allocation(request: MarketingOptimizationRequest) -> MarketingOptimizationResponse:
        return MarketingService.optimize_marketing(request)
