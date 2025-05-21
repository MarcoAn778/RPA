from PyPDF2 import PdfReader

reader = PdfReader('Robert Cecil Martin - Arquitetura Limpa - O Guia do Artesão para Estrutura e Design de Software.pdf')
# Ler pagina 4
page = reader.pages[3]

# Imprimindo no console o texto da pagina
print(page.extract_text())