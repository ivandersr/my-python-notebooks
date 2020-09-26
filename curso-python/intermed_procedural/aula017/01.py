def converte_numero(num):
    try:
        return float(num)
    except ValueError:
        pass


numero = converte_numero(input('Digite um número: '))

if numero is not None:
    print(numero * 5)
else:
    print('Tipo de dado inválido')
