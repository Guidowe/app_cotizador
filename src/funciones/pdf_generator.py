from fpdf import FPDF
import os   

def generate_pdf(cotiz_number, client_info, date,seller,refe_quote,concepts, total_amount):
    pdf = FPDF()
    pdf.add_page()
    logo_path = os.path.join(os.path.dirname(__file__), "../img/logo_dgm.jpg")
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=10, y=8, w=30)
        pdf.set_xy(10, 25)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 15, "Quotation", ln=True, align="C")
    pdf.ln(5)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Quotation: {cotiz_number}", ln=True)
    pdf.cell(0, 10, f"Date: {str(date)}", ln=True)
    pdf.cell(0, 10, f"Seller: {str(seller)}", ln=True)
    # Print client info nicely
    if isinstance(client_info, dict):
        pdf.cell(0, 10, f"Client: {client_info.get('empresa', '')}", ln=True)
    else:
        pdf.cell(0, 10, f"Client: {str(client_info)}", ln=True)
    pdf.cell(0, 10, f"Reference: {str(refe_quote)}", ln=True)
    pdf.ln(5)
    # Print DataFrame as a table
    if hasattr(concepts, "columns") and hasattr(concepts, "iterrows"):
        col_widths = [60, 35, 90] if len(concepts.columns) == 3 else [60] * len(concepts.columns)
        pdf.set_fill_color(200, 200, 200)
        pdf.set_font("Arial", "B", 12)
        for i, col in enumerate(concepts.columns):
            pdf.cell(col_widths[i], 10, str(col), border=1, align="C", fill=True)
        pdf.ln()
        pdf.set_font("Arial", "", 11)
        for _, row in concepts.iterrows():
            x_start = pdf.get_x()
            y_start = pdf.get_y()
            # Multi_cell for the first column (type)
            pdf.multi_cell(col_widths[0], 10, str(row[0]), border=1)
            # Calculate height used by multi_cell
            y_end = pdf.get_y()
            cell_height = y_end - y_start
            # Move to the right for the next cells
            pdf.set_xy(x_start + col_widths[0], y_start)
            # Print the rest of the columns with the same row height
            for i, item in enumerate(row[1:], start=1):
                pdf.cell(col_widths[i], cell_height, str(item), border=1)
            pdf.ln(cell_height)
    else:
        pdf.cell(0, 10, str(concepts), ln=True)
    pdf.ln(5)
    #pdf.set_font("Arial", "B", 12)
    #pdf.cell(0, 10, f"Total: ${total_amount:,.2f}", ln=True, align="R")
    #pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    TERMINOS = "* Valid for 30 days."
    pdf.multi_cell(0, 8, f"Terms:\n{TERMINOS}")
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Signature:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "By DIEGO AGUIRRE", ln=True)
    pdf.cell(0, 8, "CEO DGM FLORIDA", ln=True)

    return pdf.output(dest='S').encode('latin1')  # Return PDF as bytes