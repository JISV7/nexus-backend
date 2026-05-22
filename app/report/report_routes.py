from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.report.report_controller import ReportController
from app.report.report_schema import ReportRequest

router = APIRouter(prefix="/report", tags=["Report"])

@router.post("/generate")
async def generate_report(request: ReportRequest):
    pdf_buffer = ReportController.create_report(request)
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=nexuscore_report.pdf"}
    )
