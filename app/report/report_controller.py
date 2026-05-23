import io

from app.report.report_schema import ReportRequest
from app.report.report_service import ReportService


class ReportController:
    @staticmethod
    def create_report(request: ReportRequest) -> io.BytesIO:
        return ReportService.generate_pdf_report(request)
