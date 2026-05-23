from google import genai

from app.ai_analysis.ai_analysis_schema import AIAnalysisRequest, AIAnalysisResponse
from app.core.config import settings


class AIAnalysisService:
    @staticmethod
    def get_cto_analysis(request: AIAnalysisRequest) -> AIAnalysisResponse:
        # Explicitly pass the API key from settings to ensure it's loaded
        with genai.Client(api_key=settings.GEMINI_API_KEY) as client:
            prompt = f"""
            Analiza los resultados de optimización adjuntos. 
            Actúa como un LLM en el rol de CTO de NexusCore Systems.
            Tu respuesta DEBE seguir estrictamente esta estructura y tono técnico:

            1. RESUMEN EJECUTIVO (Máximo 3 líneas)
            2. ANÁLISIS DE CARGA DE SERVIDORES (Riesgo de memoria y prioridad)
            3. COMPETITIVIDAD DE RED (Evaluación de latencia vs industria)
            4. EFICIENCIA DE MARKETING (ROI y saturación)
            5. CONCLUSIÓN TÉCNICA FINAL

            DATOS DE ENTRADA:
            - Carga: {request.server_load_results}
            - Red: {request.network_routing_results}
            - Marketing: {request.marketing_optimization_results}

            REGLAS DE FORMATO:
            - NO incluyas encabezados de memorándum humano (DE:, PARA:, FECHA:, ASUNTO:).
            - NO incluyas introducciones cordiales ni saludos (ej. "Estimado equipo").
            - Usa un tono técnico, directo y basado en datos.
            - Firma al final EXACTAMENTE como: "LLM Chief Technology Officer (CTO)"
            """

            try:
                # Primary choice: gemini-flash-latest
                response = client.models.generate_content(
                    model="models/gemini-flash-latest", contents=prompt
                )
            except Exception:
                # Last resort fallback: gemini-flash-lite-latest
                response = client.models.generate_content(
                    model="models/gemini-flash-lite-latest", contents=prompt
                )

            return AIAnalysisResponse(analysis=response.text or "")
