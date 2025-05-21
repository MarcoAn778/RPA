from PyPDF2 import PdfMerger

meger = PdfMerger()
# Loop para juntar os arquivos
for pdf in ['TestePdf.pdf', 'teste_pypdf2.pdf', 'recibo_venda.pdf'] :
    meger.append(pdf)

# Salvando um novo arquivo
with open('merged-pdf.pdf', 'wb') as m:
    meger.write(m)