import sys
import time

lista = list(range(1000))


def gerador():
    for n in range(1000):
        yield n
        time.sleep(0.1)


g = gerador()

print(f'Tamanho da lista: {sys.getsizeof(lista)}')
print(f'Tamanho do gerador: {sys.getsizeof(g)}')
