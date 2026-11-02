"""Runs a scripted session of the program (inputs are echoed like a real
terminal) and renders the genuine console transcript to sample_output.txt and
Project_Output.pdf."""
import builtins, io, contextlib, re
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import employee_management as app

SCRIPT = [
    "1", "John Doe", "30",
    "2", "Jane Smith", "28", "E123", "50000",
    "3", "Alice Johnson", "40", "M456", "80000", "Sales",
    "4", "Bob Lee", "25", "D789", "65000", "Python",
    "2", "Tom Hardy", "abc", "-5", "28", "E124", "50k", "52000",   # invalid input demo
    "5", "1",
    "5", "2",
    "5", "3",
    "5", "4",
    "7",                                              # invalid menu option
    "6",
]
it = iter(SCRIPT)
buf = io.StringIO()

def fake_input(prompt=""):
    value = next(it)
    print(f"{prompt}{value}")       # echo like a terminal
    return value

builtins.input = fake_input
with contextlib.redirect_stdout(buf):
    app.main()
text = buf.getvalue()
open("sample_output.txt", "w").write(text)

# ---- render PDF ----------------------------------------------------------
W, H = A4
c = canvas.Canvas("Project_Output.pdf", pagesize=A4)
c.setTitle("Employee Management System - Program Output")
BG, FG, ORANGE = HexColor("#1e1e1e"), HexColor("#d4d4d4"), HexColor("#ff9d3d")
GREEN = HexColor("#6ad17a")
FS, LH, M = 8.5, 11.2, 40
top = H - 90

def page_header(n):
    c.setFillColor(HexColor("#ffffff")); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(HexColor("#111111")); c.setFont("Helvetica-Bold", 16)
    c.drawString(M, H - 45, "Python OOP Project: Employee Management System")
    c.setFont("Helvetica", 10); c.setFillColor(HexColor("#555555"))
    c.drawString(M, H - 62, "Program Output (console transcript of a real run)")
    c.drawRightString(W - M, 25, f"Page {n}")
    c.setFillColor(BG); c.roundRect(M - 10, 40, W - 2 * M + 20, H - 90 - 30 + 2, 6, fill=1, stroke=0)

page = 1; page_header(page); y = top
for line in text.split("\n"):
    if y < 60:
        c.showPage(); page += 1; page_header(page); y = top
    m = re.match(r"^(.*?: )(.+)$", line)
    is_prompt = line.startswith(("Enter ", "\nEnter ")) or line.startswith("Enter")
    if is_prompt and m:
        c.setFillColor(FG); c.setFont("Courier", FS); c.drawString(M, y, m.group(1))
        w = c.stringWidth(m.group(1), "Courier", FS)
        c.setFillColor(ORANGE); c.drawString(M + w, y, m.group(2))
    else:
        c.setFillColor(GREEN if line.startswith("---") else FG)
        c.setFont("Courier", FS); c.drawString(M, y, line)
    y -= LH
c.save()
print("done, pages:", page)
