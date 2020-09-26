# def funcao(texto='Oi', nome='Usuário'):
#     texto = texto.replace('a', '@')
#     nome = nome.replace('a', '@')
#     return f'{texto} {nome}'
#
#
# variavel = funcao('Hello', 'Python')
# print(variavel)

# def divisao(n1, n2):
#     if n2 == 0:
#         return
#
#     return n1 / n2
#
#
# resultado = divisao(9, 0)
#
# if resultado:
#     print(resultado)
# else:
#     print('Operação inválida')

def funcao1(var):
    print(var)


def funcao2():
    return funcao1


resultado = funcao2()
print(id(resultado), id(funcao1))
