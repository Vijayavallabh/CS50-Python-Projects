from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 8, 33)
        self.set_font("helvetica", "B", 15)
        self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
        self.ln(20)

pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)
pdf.cell(0, 10, f"{input('Name: ')} took CS50", new_x="LMARGIN", new_y="NEXT")
pdf.output("shirtificate.pdf")
