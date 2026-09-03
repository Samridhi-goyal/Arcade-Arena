from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from database.db_manager import DBManager
from tkinter import messagebox


def export_pdf(username):
    db = DBManager()
    data = db.get_user_stats(username)

    if not data:
        messagebox.showinfo("No Data", "No data found!")
        return

    doc = SimpleDocTemplate(f"{username}_report.pdf")
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph(f"{username}'s Performance Report", styles['Title']))
    elements.append(Spacer(1, 20))

    for game, score in data:
        elements.append(Paragraph(f"Game: {game}", styles['Heading3']))
        elements.append(Paragraph(f"Score: {score}", styles['Normal']))
        elements.append(Spacer(1, 10))

    doc.build(elements)

    messagebox.showinfo("Success", "PDF created successfully!")
