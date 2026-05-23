from app.marketing.marketing_schema import (
    MarketingOptimizationRequest,
    MarketingOptimizationResponse,
)
from app.marketing.marketing_service import MarketingService


class MarketingController:
    @staticmethod
    def calculate_marketing_allocation(
        request: MarketingOptimizationRequest,
    ) -> MarketingOptimizationResponse:
        return MarketingService.optimize_marketing(request)
