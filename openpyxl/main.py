import openpyxl
from random import uniform

"""
pedidos = openpyxl.load_workbook('pedidos.xlsx', data_only=True)

nome_planilhas = pedidos.sheetnames

planilha1 = pedidos['Página1']

planilha1['b3'].value = 20000  # Altera valor apenas em tempo de execução, não alterando a planilha original

for linha in range(5, 16):
    planilha1.cell(linha, 1).value = linha - 1
    planilha1.cell(linha, 2).value = 1200 + linha
    planilha1.cell(linha, 3).value = round(uniform(10, 1000), 2)


for linha in planilha1:
    for celula in linha:
        if celula.value:
            print(celula.value, end='\t')

    if linha[0].value:
        print()

pedidos.save('novos_pedidos.xlsx')
"""

planilha = openpyxl.Workbook()
planilha.create_sheet('Planilha 1', 0)
planilha.create_sheet('Planilha 2', 1)

planilha1 = planilha['Planilha 1']
planilha2 = planilha['Planilha 2']

for linha in range(1, 11):
    planilha1.cell(linha, 1).value = linha - 1
    planilha1.cell(linha, 2).value = 1200 + linha
    planilha1.cell(linha, 3).value = round(uniform(10, 1000), 2)

for linha in range(1, 11):
    planilha2.cell(linha, 1).value = linha - 1
    planilha2.cell(linha, 2).value = 1313 + linha
    planilha2.cell(linha, 3).value = round(uniform(0, 50), 2)

planilha.save('nova_planilha.xlsx')
