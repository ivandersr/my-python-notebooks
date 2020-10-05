import PyPDF2
import os

caminho_pdfs = 'pdf'

# União de vários arquivos em um único pdf
"""
novo_pdf = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_pdfs):
    for file in files:
        caminho_completo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_pdfs}/novo.pdf', 'wb') as novo:
    novo_pdf.write(novo)
"""

with open('pdf/novo.pdf', 'rb') as pdf:
    reader = PyPDF2.PdfFileReader(pdf)
    num_paginas = reader.getNumPages()

    for num_pagina in range(num_paginas):
        writer = PyPDF2.PdfFileWriter()
        pagina_atual = reader.getPage(num_pagina)
        writer.addPage(pagina_atual)

        with open(f'novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            writer.write(novo_pdf)
