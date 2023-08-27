import os

import webbrowser

from fpdf import FPDF


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("otherfiles/house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=1, align="C", ln=1)

        # Insert Period label and the value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=1, ln=1)

        os.chdir("otherfiles")

        pdf.output(self.filename)

        webbrowser.open(self.filename)
