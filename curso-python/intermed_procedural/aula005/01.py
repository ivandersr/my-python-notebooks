clientes = {
    'cliente1': {
        'nome': 'Ivander',
        'idade': 29,
    },
    'cliente2': {
        'nome': 'Jão',
        'idade': 92,
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for k, v in clientes_v.items():
        print(f'\t{k}: {v}')


# Exibindo cliente1
# 	nome: Ivander
# 	idade: 29
# Exibindo cliente2
# 	nome: Jão
# 	idade: 92