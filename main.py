from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv', sep=',')
df.sort_values(by='Order', inplace=True)
counter = 1
count_rows = df.shape[0]
print(df.iloc[0]['Pages'])

pdf = FPDF(orientation='P', unit='mm', format='A4')
# Adding topics
for i in range(count_rows):
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=20)
    pdf.cell(w=0, h=12, txt=f'{df.iloc[i]['Topic'].title()}', align='L', ln=1, border=0)
    pdf.line(10, 20, 200, 20)
    pdf.set_font(family='Times', style='B', size=10)
    pdf.ln(242)
    pdf.cell(w=0, h=12, txt=f'{counter}', align='C', ln=1, border=0)
    counter += 1
    # Adding blank pages
    for page_count in range(df.iloc[0]['Pages'] - 1):
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=10)
        pdf.ln(254)
        pdf.cell(w=0, h=12, txt=f'{counter}', align='C', ln=1, border=0)
        counter += 1

pdf.output('output.pdf')
