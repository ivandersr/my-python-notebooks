from itertools import count

indice = count()
cidades = ['Maringá', 'Belo Horizonte', 'Salvador', 'Outra cidade']
estados = ['PR', 'MG', 'BA']

cidades_estados = zip(
    indice,
    cidades,
    estados,
)

for indice, cidade, estado in cidades_estados:
    print(f'Cidade {indice}: {cidade} fica no estado {estado}')

# Cidade 0: Maringá fica no estado PR
# Cidade 1: Belo Horizonte fica no estado MG
# Cidade 2: Salvador fica no estado BA
