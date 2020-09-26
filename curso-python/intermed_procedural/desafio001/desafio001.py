# 1
def saudacao(cump, nome):
    return f'{cump}, {nome}!'


# 2
def soma(n1, n2, n3):
    return n1 + n2 + n3


# 3
def montante(valor, percent):
    return (1 + percent/100) * valor


# 4
def fizz_buzz(valor):
    return 'FizzBuzz' if valor % 5 == 0 and valor % 3 == 0 else (
        'fizz' if valor % 2 == 0 else (
            'buzz' if valor % 5 == 0 else valor
        )
    )
