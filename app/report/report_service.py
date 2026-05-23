import io

from fpdf import FPDF

from app.report.report_schema import ReportRequest


class ReportService:
    @staticmethod
    def generate_pdf_report(request: ReportRequest) -> io.BytesIO:
        pdf = FPDF()
        pdf.add_page()

        # Helper for handling text encoding if needed (fpdf2 handles unicode well with standard fonts mostly for basic latin)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(
            0,
            10,
            "Reporte Técnico de Optimización - NexusCore Systems",
            ln=True,
            align="C",
        )
        pdf.ln(5)

        # Section 1: Server Load
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "1. Optimización de Carga de Servidores", ln=True)
        pdf.set_font("Helvetica", "", 12)
        res_sl = request.server_load_results
        pdf.cell(0, 8, f"Valor de Prioridad Total: {res_sl.get('max_value')}", ln=True)
        pdf.cell(0, 8, f"RAM Total Utilizada: {res_sl.get('total_weight')} GB", ln=True)
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, "Microservicios Desplegados:", ln=True)
        pdf.set_font("Helvetica", "", 11)
        for item in res_sl.get("selected_items", []):
            pdf.cell(10)  # indent
            pdf.cell(
                0,
                6,
                f"- {item['name']} (RAM: {item['weight']} GB, Prioridad: {item['value']})",
                ln=True,
            )
        pdf.ln(5)

        # Section 2: Network Routing
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "2. Red de Distribución de Datos", ln=True)
        pdf.set_font("Helvetica", "", 12)
        res_nr = request.network_routing_results
        pdf.cell(0, 8, f"Latencia Mínima: {res_nr.get('min_latency')} ms", ln=True)
        pdf.cell(0, 8, f"Ruta Crítica: {' -> '.join(res_nr.get('path', []))}", ln=True)
        pdf.ln(5)

        # Section 3: Marketing
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "3. Optimización de Marketing", ln=True)
        pdf.set_font("Helvetica", "", 12)
        res_mkt = request.marketing_optimization_results
        pdf.cell(0, 8, f"Usuarios Estimados: {res_mkt.get('max_value')} K", ln=True)
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, "Asignación de Presupuesto:", ln=True)
        pdf.set_font("Helvetica", "", 11)

        channels = res_mkt.get("channels", [])
        if channels:
            for ch in channels:
                investment = ch.get("investment", 0) * 1000
                pdf.cell(10)  # indent
                pdf.cell(0, 6, f"- {ch.get('name')}: ${investment:,.2f}", ln=True)
        else:
            # Fallback for older results
            x1 = res_mkt.get("x1", 0) * 1000
            x2 = res_mkt.get("x2", 0) * 1000
            pdf.cell(10)
            pdf.cell(0, 6, f"- Creadores de Contenido (x1): ${x1:,.2f}", ln=True)
            pdf.cell(10)
            pdf.cell(0, 6, f"- Anuncios Programáticos (x2): ${x2:,.2f}", ln=True)

        pdf.ln(8)

        # Section 4: AI Analysis
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Conclusiones Estratégicas del Asistente de IA", ln=True)
        pdf.set_font("Helvetica", "", 11)

        # Clean unicode characters that Helvetica doesn't support well in FPDF
        ai_text = (
            request.ai_analysis.replace("\u201c", '"')
            .replace("\u201d", '"')
            .replace("\u2018", "'")
            .replace("\u2019", "'")
        )
        ai_text = (
            ai_text.replace("\u2013", "-")
            .replace("\u2014", "-")
            .replace("\u2026", "...")
        )

        # Multi_cell handles text wrapping
        pdf.multi_cell(0, 6, ai_text)

        # Output to buffer
        pdf_buffer = io.BytesIO()
        pdf_output = pdf.output()
        pdf_buffer.write(pdf_output)
        pdf_buffer.seek(0)

        return pdf_buffer
