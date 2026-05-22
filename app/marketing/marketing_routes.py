from fastapi import APIRouter
from app.marketing.marketing_controller import MarketingController
from app.marketing.marketing_schema import MarketingOptimizationRequest, MarketingOptimizationResponse

router = APIRouter(prefix="/marketing", tags=["Marketing"])

@router.post("/optimize", response_model=MarketingOptimizationResponse)
async def optimize_marketing(request: MarketingOptimizationRequest):
    return MarketingController.calculate_marketing_allocation(request)
