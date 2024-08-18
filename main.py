from fpdf import FPDF
import pandas as pd


class FPDF(FPDF):
    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        page_num = self.page_no()
        # Print centered page number
        self.cell(0, 10, str(page_num), 0, 0, 'C')


df = pd.read_csv('topics.csv', sep=',')
df.sort_values(by='Order', inplace=True)
count_rows = df.shape[0]

pdf = FPDF(orientation='P', unit='mm', format='A4')
# Adding topics
for i in range(count_rows):
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=20)
    pdf.cell(w=0, h=12, txt=f'{df.iloc[i]['Topic'].title()}', align='L', ln=1, border=0)
    pdf.line(10, 20, 200, 20)
    pdf.set_font(family='Times', style='I', size=10)
    pdf.multi_cell(w=0, h=5, txt=f'{df.iloc[i]['Text']}', align='L', border=0)
    # Adding blank pages
    for page_count in range(df.iloc[0]['Pages'] - 1):
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=10)

pdf.output('output.pdf')
