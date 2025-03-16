from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import letter

# Define function to generate invoice
def generate_invoice(filename, invoice_details):
    # Set up PDF document
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()

    # Custom style for title and header
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        spaceAfter=12,
        alignment=1,
        textColor=colors.darkblue
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=12,
        alignment=1,
        textColor=colors.darkgrey
    )

    body_style = styles['Normal']
    body_style.fontName = 'Helvetica'
    body_style.fontSize = 10

    # Elements to add to the document
    elements = []

    # Header - Company Information
    elements.append(Paragraph("<b>DevTech</b>", title_style))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph("123 Business Ave, City, Country", subtitle_style))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph("Phone: (123) 456-7890 | Email: info@company.com", subtitle_style))
    elements.append(Spacer(1, 12))  # Spacer between header and title

    # Invoice Title
    elements.append(Paragraph("<b>Invoice</b>", title_style))
    elements.append(Spacer(1, 12))

    # Add the invoice details (e.g., invoice number, date)
    elements.append(Paragraph(f"<b>Invoice Number:</b> {invoice_details['Invoice Number']}", body_style))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(f"<b>Invoice Date:</b> {invoice_details['Invoice Date']}", body_style))
    elements.append(Spacer(1, 12))  # Spacer between invoice details and table

    # Create a table for logistics details
    data = [['Key', 'Value']]  # Table header row
    for key, value in invoice_details.items():
        if key not in ['Invoice Number', 'Invoice Date']:  # Avoid duplicate fields
            data.append([key, value])

    table = Table(data, colWidths=[200, 300], rowHeights=25)
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Grid lines
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Header background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Body font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),  # Alternating row color
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Total Cost Section (highlight this part)
    elements.append(Paragraph(f"<b>Total Cost:</b> {invoice_details['Cost']}", body_style))
    elements.append(Spacer(1, 12))

    # Footer - Page Number
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 10)
        canvas.drawString(500, 10, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)

# Example invoice data
invoice_data = {
    "Invoice Number": "12345",
    "Invoice Date": "March 10, 2025",
    "Shipment Type": "Containerized",
    "Origin": "Los Angeles, USA",
    "Destination": "Shanghai, China",
    "Number of Containers": "15",
    "Tonnage": "3000 tons",
    "Cost": "$50,000",
    "Route": "Pacific Ocean"
}

# Generate the invoice PDF
#generate_invoice("logistics_invoice_professional.pdf", invoice_data)
