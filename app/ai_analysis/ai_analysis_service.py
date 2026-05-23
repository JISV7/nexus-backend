import httpx
from fastapi import HTTPException
from google import genai

from app.ai_analysis.ai_analysis_schema import AIAnalysisRequest, AIAnalysisResponse
from app.core.config import settings


class AIAnalysisService:
    @staticmethod
    def get_cto_analysis(request: AIAnalysisRequest) -> AIAnalysisResponse:
        # Explicitly pass the API key from settings to ensure it's loaded
        try:
            with genai.Client(api_key=settings.GEMINI_API_KEY) as client:
                # Format data strings or 'SKIP' message
                sl_data = (
                    request.server_load_results
                    if request.server_load_results
                    else "DATOS NO DISPONIBLES (OMITIR ANÁLISIS)"
                )
                nr_data = (
                    request.network_routing_results
                    if request.network_routing_results
                    else "DATOS NO DISPONIBLES (OMITIR ANÁLISIS)"
                )
                mkt_data = (
                    request.marketing_optimization_results
                    if request.marketing_optimization_results
                    else "DATOS NO DISPONIBLES (OMITIR ANÁLISIS)"
                )

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
                - Carga: {sl_data}
                - Red: {nr_data}
                - Marketing: {mkt_data}

                REGLAS IMPORTANTES:
                - Si algún dato de entrada dice "DATOS NO DISPONIBLES", indica explícitamente en el punto correspondiente que el análisis fue OMITIDO por falta de datos.
                - NO incluyas encabezados de memorándum humano (DE:, PARA:, FECHA:, ASUNTO:).
                - NO incluyas introducciones cordiales ni saludos.
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
                    # If this fails, it will be caught by the outer try-except
                    response = client.models.generate_content(
                        model="models/gemini-flash-lite-latest", contents=prompt
                    )

                return AIAnalysisResponse(analysis=response.text or "")
        except (httpx.ConnectError, httpx.ConnectTimeout):
            raise HTTPException(
                status_code=503,
                detail="Error de conexión: No se pudo contactar con el servicio de IA. Por favor, verifica tu conexión a internet.",
            )
        except Exception as e:
            # Re-raise as HTTPException to avoid crashing the server
            raise HTTPException(
                status_code=500,
                detail=f"Error inesperado al generar el análisis de IA: {str(e)}",
            )
