from intermed_procedural.aula014.dados import produtos, pessoas, lista


nova_lista = filter(lambda p: p['preco'] > 10, produtos)

for produto in nova_lista:
    print(produto)

# {'nome': 'p1', 'preco': 50}
# {'nome': 'p2', 'preco': 13}
# {'nome': 'p3', 'preco': 50.51}
# {'nome': 'p5', 'preco': 45}
# {'nome': 'p7', 'preco': 89.99}
# {'nome': 'p8', 'preco': 12}