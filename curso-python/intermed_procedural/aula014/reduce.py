from intermed_procedural.aula014.dados import pessoas, produtos, lista
from functools import reduce

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)

print(f'A média de preço é R$ {soma_precos/len(produtos):.2f}')
