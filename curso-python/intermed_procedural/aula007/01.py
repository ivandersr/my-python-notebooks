# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = [(v, v2) for v in l1 for v2 in range(3)]
#
# print(l2)

# l1 = ['Maria', 'João', 'Mauro']
# l2 = [v.replace('a', '@') for v in l1]
#
# print(l2)

# tupla = (
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# )
#
# lista = [(y, x) for x, y in tupla]
# print(lista)

lista = list(range(31))
div_2_3 = [v if not v % 2 and not v % 3 else 0 for v in lista]

print(div_2_3)
