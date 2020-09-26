from vendas.format.preco import real


def aumentar(valor, percentagem, formatar=False):
    r = valor * (1 + percentagem / 100)
    if formatar:
        return real(r)
    else:
        return r


def descontar(valor, percentagem, formatar=False):
    r = valor * (1 - percentagem / 100)
    if formatar:
        return real(r)
    else:
        return r
