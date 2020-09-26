lista = [0, 1, 2, 3, 4, 5, 6]
lista = iter(lista)

print(lista)
print(hasattr(lista, '__next__'))
