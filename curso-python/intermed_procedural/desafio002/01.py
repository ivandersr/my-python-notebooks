def funcao1(arg):
    return arg()


def funcao2():
    valor = 'Função 2 executada'
    return valor


print(funcao1(funcao2))
