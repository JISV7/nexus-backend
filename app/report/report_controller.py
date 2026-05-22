from app.report.report_service import ReportService
from app.report.report_schema import ReportRequest
import io

class ReportController:
    @staticmethod
    def create_report(request: ReportRequest) -> io.BytesIO:
        return ReportService.generate_pdf_report(request)
