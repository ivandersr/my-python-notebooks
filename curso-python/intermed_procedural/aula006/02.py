lista1 = [1, 2, 3, 4, 3, 2, 3, 4, 5, 'teste', 'teste']
lista2 = [5, 2, 3, 6, 3, 4, 7, 4, 1, 'teste', 'teste2']

lista_resultante = set(lista1)
lista_resultante.update(lista2)

lista_resultante = list(lista_resultante)

print(lista_resultante)
