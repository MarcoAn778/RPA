from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader('TestePdf.pdf')
writer = PdfWriter()

#Adicionando as páginas para escrita
for page in reader.pages :
    writer.add_page(page)

#Adicionando uma senha ao novo pdf
writer.encrypt('senha')

# Salvando o novo pdf em um arquivo
with open('encrypted-pdf.pdf', 'wb') as e :
    writer.write(e)

