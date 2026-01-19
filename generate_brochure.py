from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.pdfgen import canvas
import os

# Define Contoso colors
CONTOSO_BLUE = colors.HexColor("#2F8ACE")
CONTOSO_GOLD = colors.HexColor("#FFB201")
CONTOSO_SECONDARY = colors.HexColor("#1a5f8a")

def create_mba_brochure():
    """Create a professional MBA brochure PDF"""
    
    # Create PDF
    pdf_filename = "MBA_Digital_Transformation_AI_Leadership_Brochure.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=A4,
                           rightMargin=50, leftMargin=50,
                           topMargin=50, bottomMargin=50)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=CONTOSO_BLUE,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=CONTOSO_SECONDARY,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=CONTOSO_BLUE,
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        leading=16
    )
    
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['BodyText'],
        fontSize=11,
        spaceAfter=8,
        leftIndent=20,
        leading=14
    )
    
    # Add logo if exists
    logo_path = "img/4.Contoso_uni_Logo_Scritta_horizontal.png"
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=4*inch, height=1*inch)
        logo.hAlign = 'CENTER'
        elements.append(logo)
        elements.append(Spacer(1, 20))
    
    # Title
    elements.append(Paragraph("MBA in Digital Transformation & AI Leadership", title_style))
    elements.append(Spacer(1, 10))
    
    # Tagline
    elements.append(Paragraph("Lead business transformation through data‑driven strategy, AI, and modern leadership", subtitle_style))
    elements.append(Spacer(1, 5))
    
    # Location
    location_style = ParagraphStyle('Location', parent=styles['Normal'], fontSize=12, alignment=TA_CENTER, textColor=CONTOSO_SECONDARY)
    elements.append(Paragraph("📍 Contoso University, Monteverde, Italy", location_style))
    elements.append(Spacer(1, 25))
    
    # Program Overview Section
    elements.append(Paragraph("Program Overview", heading_style))
    
    overview_text = """The MBA in Digital Transformation & AI Leadership is designed for professionals who want to accelerate their careers by mastering the strategic, organizational, and leadership implications of digital innovation and artificial intelligence."""
    elements.append(Paragraph(overview_text, body_style))
    
    overview_text2 = """The program focuses on how emerging technologies reshape business models, customer experiences, and decision‑making processes, preparing participants to lead transformation initiatives across industries."""
    elements.append(Paragraph(overview_text2, body_style))
    
    overview_text3 = """Blending strategy, technology, and leadership, the MBA equips participants with the mindset and tools needed to navigate complexity, drive change, and create sustainable business value in an AI‑driven economy."""
    elements.append(Paragraph(overview_text3, body_style))
    elements.append(Spacer(1, 15))
    
    # Target Audience Section
    elements.append(Paragraph("Who Should Apply", heading_style))
    
    # Create a table for the two audiences
    audience_data = [
        [Paragraph("<b>Experienced Professionals & Alumni</b>", body_style), 
         Paragraph("<b>Prospective Students</b>", body_style)],
        [Paragraph("• 5+ years of professional experience<br/>• Seeking career acceleration and leadership roles<br/>• Interested in digital and AI‑driven initiatives", bullet_style),
         Paragraph("• Graduates exploring MBA options<br/>• Interested in digital transformation and AI<br/>• Looking for an English‑taught program", bullet_style)]
    ]
    
    audience_table = Table(audience_data, colWidths=[3.5*inch, 3.5*inch])
    audience_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), CONTOSO_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(audience_table)
    elements.append(Spacer(1, 20))
    
    # Key Learning Areas
    elements.append(Paragraph("Key Learning Areas", heading_style))
    
    learning_areas = [
        "Digital Strategy & Business Transformation",
        "Artificial Intelligence for Business Leaders",
        "Data‑Driven Decision Making",
        "Customer Experience & Growth",
        "Leadership, Change & Organizational Impact"
    ]
    
    for area in learning_areas:
        elements.append(Paragraph(f"• {area}", bullet_style))
    
    elements.append(Spacer(1, 20))
    
    # Career Outcomes
    elements.append(Paragraph("Career Outcomes", heading_style))
    elements.append(Paragraph("Graduates of the program typically pursue roles such as:", body_style))
    
    careers = [
        "Digital Transformation Manager",
        "AI & Data Strategy Lead",
        "Product or Innovation Manager",
        "Business Consultant",
        "Future General Manager or Entrepreneur"
    ]
    
    for career in careers:
        elements.append(Paragraph(f"• {career}", bullet_style))
    
    elements.append(Spacer(1, 25))
    
    # Page Break
    elements.append(PageBreak())
    
    # Add logo on second page
    if os.path.exists(logo_path):
        logo2 = Image(logo_path, width=3*inch, height=0.75*inch)
        logo2.hAlign = 'CENTER'
        elements.append(logo2)
        elements.append(Spacer(1, 20))
    
    # Webinar Information
    elements.append(Paragraph("Join Our Information Webinar", heading_style))
    
    webinar_title_style = ParagraphStyle('WebinarTitle', parent=styles['Normal'], fontSize=14, alignment=TA_CENTER, 
                                         textColor=CONTOSO_BLUE, fontName='Helvetica-Oblique', spaceAfter=15)
    elements.append(Paragraph('"From Digital Transformation to AI Leadership: How an MBA Can Accelerate Your Career"', webinar_title_style))
    
    # Webinar Date/Time
    datetime_style = ParagraphStyle('DateTime', parent=styles['Normal'], fontSize=13, alignment=TA_CENTER, 
                                   textColor=CONTOSO_SECONDARY, fontName='Helvetica-Bold', spaceAfter=15)
    elements.append(Paragraph("📅 February 27, 2026 | ⏰ 5:00 PM - 6:00 PM (CET)", datetime_style))
    
    elements.append(Paragraph("What You'll Learn:", body_style))
    
    webinar_topics = [
        "MBA structure and value proposition",
        "Career outcomes and success stories",
        "Admissions process and requirements",
        "Live Q&A with faculty and admissions team",
        "Next steps for your application journey"
    ]
    
    for topic in webinar_topics:
        elements.append(Paragraph(f"• {topic}", bullet_style))
    
    elements.append(Spacer(1, 25))
    
    # Next Steps
    elements.append(Paragraph("Take the Next Step", heading_style))
    
    next_steps_data = [
        ["📅 Register for Webinar", "📄 Download Brochure", "💬 Book Consultation"],
        ["Join our information session", "Get detailed information", "Schedule a 1:1 call with admissions"],
    ]
    
    steps_table = Table(next_steps_data, colWidths=[2.3*inch, 2.3*inch, 2.3*inch])
    steps_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), CONTOSO_GOLD),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, CONTOSO_BLUE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
    ]))
    elements.append(steps_table)
    elements.append(Spacer(1, 30))
    
    # Contact Information
    elements.append(Paragraph("Contact Information", heading_style))
    
    contact_style = ParagraphStyle('Contact', parent=styles['Normal'], fontSize=11, alignment=TA_CENTER, spaceAfter=8)
    elements.append(Paragraph("<b>Contoso University</b>", contact_style))
    elements.append(Paragraph("Via della Innovazione, 42 - 20100 Monteverde (MV), Italy", contact_style))
    elements.append(Paragraph("Email: mba@contosouniversity.it | Phone: +39 045 123 4567", contact_style))
    elements.append(Spacer(1, 20))
    
    # Footer
    footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=9, alignment=TA_CENTER, 
                                  textColor=colors.grey)
    elements.append(Paragraph("© 2026 Contoso University. All rights reserved.", footer_style))
    
    # Build PDF
    doc.build(elements)
    print(f"✅ MBA brochure created successfully: {pdf_filename}")
    return pdf_filename

if __name__ == "__main__":
    create_mba_brochure()
