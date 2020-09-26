def dividir(n1, n2):
    if not n2:
        raise ValueError('O segundo argumento deve ser não-nulo')
    return n1 / n2


print(dividir(2, 0))
