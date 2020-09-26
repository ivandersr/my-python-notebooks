# string = 'Ontem comi frango no almoço. Hoje, nem comi nada :('
#
# lista_espaco = string.split(' ')
#
# frequencia = 0
# palavra = ''
# for valor in lista_espaco:
#     frequencia_atual = lista_espaco.count(valor)
#
#     if frequencia_atual > frequencia:
#         frequencia = frequencia_atual
#         palavra = valor
#
# print(f'A palavra com mais frequencia é "{palavra}", aparecendo {frequencia} vezes.')

# string_original = 'Acho que já comecei a entender Python'
# lista = string_original.split(' ')
# string = ' '.join(lista)
#
# print(string_original)
# print(lista)
# print(string)

# string = 'Acho que já comecei a entender Python'
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(f'Na posição {indice} o valor é "{valor}"')
#
lista = [
    [0, 'Ivander'],
    [1, 'Salvador'],
    [2, 'Ruiz'],
]

lista_enum = ['Ivander', 'Salvador', 'Ruiz']

for indice, nome in lista:
    print(indice, nome, sep=':', end=' - ')

print()

for indice, nome in enumerate(lista_enum):
    print(indice, nome, sep=':', end=' - ')

# [1, 2]
# [3, 4]
# [5, 6]