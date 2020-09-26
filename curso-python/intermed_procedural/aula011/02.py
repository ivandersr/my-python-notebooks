from itertools import count

lista = [1234, 53, 2, 3, 123, 7, 1234, 2]
contador = count()

lista = list(zip(contador, lista))

print(lista)
