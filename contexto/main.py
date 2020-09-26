"""class Arquivo:
    def __init__(self, arquivo, modo):
        print('init')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saiu na classe')
        self.arquivo.close()


with Arquivo('abc.txt', 'w') as arquivo:
    print('entrou no contexto')
    arquivo.write('Alguma coisa')
"""
from contextlib import contextmanager


@contextmanager
def abrir(arq, modo):
    try:
        print('Abrindo arquivo')
        arq = open(arq, modo)
        yield arq
    finally:
        print('Fechando arquivo')
        arq.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
