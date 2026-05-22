from fpdf import FPDF
import io
from app.report.report_schema import ReportRequest

class ReportService:
    @staticmethod
    def generate_pdf_report(request: ReportRequest) -> io.BytesIO:
        pdf = FPDF()
        pdf.add_page()
        
        # Header
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "Reporte Técnico de Optimización - NexusCore Systems", ln=True, align="C")
        pdf.ln(10)
        
        # Section 1: Server Load
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "1. Optimización de Carga de Servidores", ln=True)
        pdf.set_font("Helvetica", "", 12)
        res = request.server_load_results
        pdf.multi_cell(0, 10, f"Valor de Prioridad Total: {res.get('max_value')}\n"
                             f"RAM Total Utilizada: {res.get('total_weight')} GB\n"
                             f"Servidores Seleccionados: {', '.join([item['name'] for item in res.get('selected_items', [])])}")
        pdf.ln(5)
        
        # Section 2: Network Routing
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "2. Red de Distribución de Datos", ln=True)
        pdf.set_font("Helvetica", "", 12)
        res = request.network_routing_results
        pdf.multi_cell(0, 10, f"Latencia Mínima: {res.get('min_latency')} ms\n"
                             f"Ruta Crítica: {' -> '.join(res.get('path', []))}")
        pdf.ln(5)
        
        # Section 3: Marketing
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "3. Optimización de Marketing", ln=True)
        pdf.set_font("Helvetica", "", 12)
        res = request.marketing_optimization_results
        pdf.multi_cell(0, 10, f"Inversión Creadores (x1): {res.get('x1')}\n"
                             f"Inversión Programática (x2): {res.get('x2')}\n"
                             f"Usuarios Estimados (f): {res.get('max_value')}")
        pdf.ln(10)
        
        # Section 4: AI Analysis
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Conclusiones Estratégicas del Asistente de IA", ln=True)
        pdf.set_font("Helvetica", "", 11)
        # Handle unicode characters if necessary, fpdf2 usually handles it or needs a font
        pdf.multi_cell(0, 8, request.ai_analysis)
        
        # Output to buffer
        pdf_buffer = io.BytesIO()
        pdf_output = pdf.output()
        pdf_buffer.write(pdf_output)
        pdf_buffer.seek(0)
        
        return pdf_buffer
