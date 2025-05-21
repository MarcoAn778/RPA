from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader('encrypted-pdf.pdf')
wrider = PdfWriter()

# Verificando se há senha 
if reader.is_encrypted :
    reader.decrypt('senha')

# Adicionando as paginas para escrita
for page in reader.pages :
    wrider.add_page(page)

# Salvando o novo pdf
with open('decrypted-pdf.pdf', 'wb') as d:
    wrider.write(d)