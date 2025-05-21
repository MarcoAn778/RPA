from PyPDF2 import PdfReader

reader = PdfReader('Robert Cecil Martin - Arquitetura Limpa - O Guia do Artesão para Estrutura e Design de Software.pdf')
# Obter o numero de páginas
print(len(reader.pages))

#Obtendo Metadados do pdf

meta = reader.metadata
print(meta.author)
print(meta.creator)
print(meta.producer)
print(meta.subject)
print(meta.title)