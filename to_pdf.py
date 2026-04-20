from table import create_table

from fpdf import FPDF
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode

base = 10
digits = 8

# Instantiation of inherited class
pdf = FPDF(format="Letter")

pdf.add_page()
pdf.set_font("times", size=9)
pdf.set_draw_color(255, 0, 0)
pdf.set_line_width(0.3)
headings_style = FontFace(emphasis="BOLD", color=255, fill_color=(255, 100, 0))
with pdf.table(
    borders_layout="SINGLE_TOP_LINE",
    headings_style=headings_style,
    line_height=5.8,
    text_align=("LEFT", "LEFT", "LEFT", "LEFT", "LEFT", "LEFT", "LEFT", "LEFT"),
    width=160,
    first_row_as_headings=False,
) as table:
    for i in range(0, 10):
        for row in range(1, 26):
            table_start = i * 100 + row * 4 - 3
            data_row = create_table(1, 4, base, table_start, digits)
            table_row = table.row()
            for datum in data_row[0]:
                table_row.cell(datum)


        
pdf.output(f"log_table_base{base}.pdf")