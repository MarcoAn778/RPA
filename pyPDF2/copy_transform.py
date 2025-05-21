from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader('Robert Cecil Martin - Arquitetura Limpa - O Guia do Artesão para Estrutura e Design de Software.pdf')
wrider = PdfWriter()

#Adicionar uma página ao pdf
wrider.add_page(reader.pages[0])

#Adicionar a página 2 de um arquivo ao pdf rotacionada em 90°
page2 = reader.pages[1]
page2.rotate(90)
wrider.add_page(page2)

#Adicionar a página 3 cortada pela metadata
page3 = reader.pages[2]
page3.mediabox.upper_right = (
    page3.mediabox.right / 2,
    page3.mediabox.top / 2
)

wrider.add_page(page3)


# Escrevendo e salvando o documento pdf

with open('pydef_copy_transform.pdf', 'wb') as p:
    wrider.write(p)
