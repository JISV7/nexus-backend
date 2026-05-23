from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.ai_analysis.ai_analysis_routes import router as ai_analysis_router
from app.core.config import settings
from app.marketing.marketing_routes import router as marketing_router
from app.network_routing.network_routing_routes import router as network_routing_router
from app.report.report_routes import router as report_router
from app.server_load.server_load_routes import router as server_load_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers

app.include_router(server_load_router, prefix=settings.API_V1_STR)
app.include_router(network_routing_router, prefix=settings.API_V1_STR)
app.include_router(marketing_router, prefix=settings.API_V1_STR)
app.include_router(ai_analysis_router, prefix=settings.API_V1_STR)
app.include_router(report_router, prefix=settings.API_V1_STR)


@app.api_route("/", methods=["GET", "HEAD"])
async def root():
    return {"message": "Welcome to NexusCore API", "version": settings.VERSION}


if __name__ == "__main__":
    import os

    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
