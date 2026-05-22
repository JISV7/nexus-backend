from google import genai
from app.core.config import settings
from app.ai_analysis.ai_analysis_schema import AIAnalysisRequest, AIAnalysisResponse

class AIAnalysisService:
    @staticmethod
    def get_cto_analysis(request: AIAnalysisRequest) -> AIAnalysisResponse:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        
        prompt = f"""
        Actúa como un Chief Technology Officer (CTO) de NexusCore Systems.
        Analiza la viabilidad de negocio y el riesgo técnico de los siguientes resultados de optimización:

        1. Optimización de Carga de Servidores:
        {request.server_load_results}

        2. Red de Distribución de Datos (Latencia):
        {request.network_routing_results}

        3. Optimización de Presupuesto de Marketing:
        {request.marketing_optimization_results}

        Exige un análisis sobre:
        - Si la latencia obtenida es competitiva en la industria actual.
        - El riesgo técnico de la distribución de memoria seleccionada.
        - La eficiencia del retorno de inversión en marketing digital ante los rendimientos decrecientes.
        
        Formatea tu respuesta de forma clara y profesional.
        """
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        
        return AIAnalysisResponse(analysis=response.text)
