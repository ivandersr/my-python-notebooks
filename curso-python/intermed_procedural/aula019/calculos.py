import math

PI = math.pi


def dobra_lista(arg):
    return [x * 2 for x in arg]


def multiplica_lista(arg):
    result = 1
    for i in arg:
        result *= i
    return result


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica_lista(lista))
    print(PI)
