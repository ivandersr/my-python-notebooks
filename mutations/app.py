def lista_clientes(clientes_iteravel, lista=None):
    if not lista:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_clientes(['a', 'b', 'c'])
clientes2 = lista_clientes(['d', 'e', 'f'])

print(clientes1)
print(clientes2)
