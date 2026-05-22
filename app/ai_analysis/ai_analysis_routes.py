from fastapi import APIRouter
from app.ai_analysis.ai_analysis_controller import AIAnalysisController
from app.ai_analysis.ai_analysis_schema import AIAnalysisRequest, AIAnalysisResponse

router = APIRouter(prefix="/ai-analysis", tags=["AI Analysis"])

@router.post("/generate", response_model=AIAnalysisResponse)
async def generate_ai_analysis(request: AIAnalysisRequest):
    return AIAnalysisController.generate_analysis(request)
