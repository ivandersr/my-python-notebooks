lista = [
    ('chave', 2),
    ('chave2', 5.4),
]

d1 = {x: y * 2 for x, y in lista}

print(d1)  # out: {'chave': 4, 'chave2': 10.8}

