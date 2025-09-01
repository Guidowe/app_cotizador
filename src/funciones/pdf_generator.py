from fpdf import FPDF
import os   

def generate_pdf(cotiz_number, client_info, concepts, total_amount):
    pdf = FPDF()
    pdf.add_page()
    logo_path = os.path.join(os.path.dirname(__file__), "../img/logo_dgm.png")
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=10, y=8, w=30)
        pdf.set_xy(10, 25)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 15, "COTIZACIÓN", ln=True, align="C")
    pdf.ln(5)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Cotización: {cotiz_number}", ln=True)
    # Print client info nicely
    if isinstance(client_info, dict):
        pdf.cell(0, 10, f"Empresa: {client_info.get('empresa', '')}", ln=True)
        pdf.cell(0, 10, f"Contacto: {client_info.get('contacto', '')}", ln=True)
        pdf.cell(0, 10, f"Referencia: {client_info.get('referencia', '')}", ln=True)
    else:
        pdf.cell(0, 10, f"Cliente: {str(client_info)}", ln=True)
    pdf.ln(5)
    # Print DataFrame as a table
    if hasattr(concepts, "columns") and hasattr(concepts, "iterrows"):
        col_widths = [40, 35, 90] if len(concepts.columns) == 3 else [60] * len(concepts.columns)
        pdf.set_fill_color(200, 200, 200)
        pdf.set_font("Arial", "B", 12)
        for i, col in enumerate(concepts.columns):
            pdf.cell(col_widths[i], 10, str(col), border=1, align="C", fill=True)
        pdf.ln()
        pdf.set_font("Arial", "", 11)
        for _, row in concepts.iterrows():
            for i, item in enumerate(row):
                pdf.cell(col_widths[i], 10, str(item), border=1, align="L")
            pdf.ln()
    else:
        pdf.cell(0, 10, str(concepts), ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Total: ${total_amount:,.2f}", ln=True, align="R")
    pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    TERMINOS = "* Válido por 30 días."
    pdf.multi_cell(0, 8, f"TÉRMINOS:\n{TERMINOS}")
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "FIRMA:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "POR DIEGO AGUIRRE", ln=True)
    pdf.cell(0, 8, "CEO DGM FLORIDA", ln=True)

    return pdf.output(dest='S').encode('latin1')  # Return PDF as bytes