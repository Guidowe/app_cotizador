from fpdf import FPDF

def generate_pdf(cotiz_number, client_info, concepts, total_amount):

    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Cotización: {cotiz_number}", ln=True)
    pdf.cell(200, 10, txt=f"Cliente: {client_info}", ln=True)
    pdf.cell(200, 10, txt=f"Total: ${total_amount}", ln=True)
    return pdf.output(dest='S').encode('latin1')  # Return PDF as bytes