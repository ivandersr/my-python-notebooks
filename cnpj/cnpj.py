from random import randint
import re


def remover_caracteres(_cnpj):
    return re.sub(r'[^0-9]', '', _cnpj)


def definir_digito(_cnpj, digito=1):
    if not _cnpj:
        return
    _cnpj = remover_caracteres(_cnpj)
    _cnpj = list(_cnpj)
    _cnpj.pop()
    lista_validadora = list(range(6, 1, -1))
    lista_validadora.extend(list(range(9, 1, -1)))

    if digito == 1:
        _cnpj.pop()
        lista_validadora.pop(0)

    lista_soma = [int(x) * y for x, y in zip(_cnpj, lista_validadora)]

    soma = sum(lista_soma)
    validacao = 11 - soma % 11

    if validacao > 9:
        return 0
    else:
        return validacao


def validar_cnpj(_cnpj):
    digito1 = definir_digito(_cnpj, 1)
    digito2 = definir_digito(_cnpj, 2)

    _cnpj = list(_cnpj)
    if int(_cnpj[-1]) == digito2 and int(_cnpj[-2]) == digito1:
        return f'CNPJ válido'
    else:
        return f'CNPJ inválido'


def preencher_bloco(bloco, digitos):
    print(len(bloco) - digitos)
    if len(bloco) < digitos:
        print(len(bloco) - digitos)
        return (len(bloco) - digitos) * '0' + bloco
    return bloco


def gerar_cnpj():
    print(randint(1, 99))
    primeiro_bloco = preencher_bloco(str(randint(1, 99)), 2)
    segundo_bloco = preencher_bloco(str(randint(1, 999)), 3)
    terceiro_bloco = preencher_bloco(str(randint(1, 999)), 3)
    quarto_bloco = '0001'

    cnpj_inicial = f'{primeiro_bloco}.{segundo_bloco}.{terceiro_bloco}/{quarto_bloco}-00'

    digito1 = definir_digito(cnpj_inicial, 1)
    digito2 = definir_digito(cnpj_inicial, 2)

    cnpj = cnpj_inicial[:-2] + str(digito1) + str(digito2)

    return cnpj

