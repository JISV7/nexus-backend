from google import genai
from app.ai_analysis.ai_analysis_schema import AIAnalysisRequest, AIAnalysisResponse

class AIAnalysisService:
    @staticmethod
    def get_cto_analysis(request: AIAnalysisRequest) -> AIAnalysisResponse:
        # Client picks up GEMINI_API_KEY or GOOGLE_API_KEY from env automatically
        with genai.Client() as client:
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
            
            try:
                # Primary choice: gemini-flash-latest
                response = client.models.generate_content(
                    model="models/gemini-flash-latest",
                    contents=prompt
                )
            except Exception:
                # Last resort fallback: gemini-flash-lite-latest
                response = client.models.generate_content(
                    model="models/gemini-flash-lite-latest",
                    contents=prompt
                )
            
            return AIAnalysisResponse(analysis=response.text)
