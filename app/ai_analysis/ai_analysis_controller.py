from app.ai_analysis.ai_analysis_schema import AIAnalysisRequest, AIAnalysisResponse
from app.ai_analysis.ai_analysis_service import AIAnalysisService


class AIAnalysisController:
    @staticmethod
    def generate_analysis(request: AIAnalysisRequest) -> AIAnalysisResponse:
        return AIAnalysisService.get_cto_analysis(request)
