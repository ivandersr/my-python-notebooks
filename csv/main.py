import csv

with open('clientes.csv', 'r') as file:
    dados = [x for x in csv.DictReader(file)]

with open('clientes2.csv', 'w', newline='') as file:
    escreve = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    escreve.writerow(list(dados[0].keys()))

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
