from collections import deque
"""
Pilha (Stack) - LIFO
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

livro_removido = livros.pop()

print(livros)
print(livro_removido)
"""

"""
Fila (Queue) - FIFO
Não é adequado trabalhar com listas para filas, pois na remoção do primeiro elemento, todos os outros
devem ter seus índices alterados. Por isso, utilizamos a collection "deque".
Caso seja definido o parâmetro "maxlen", o comprimento máximo é atribuído à coleção e, quando mais elementos 
são adicionados, o primeiro elemento será automaticamente removido para a agregação do último valor.
"""
fila = deque(maxlen=5)

fila.append('Cliente 1')
fila.append('Cliente 2')
fila.append('Cliente 3')
fila.append('Cliente 4')
fila.append('Cliente 5')

fila.append('Cliente 6')
print(fila)

