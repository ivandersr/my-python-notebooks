# cpf_raw = input('Digite o cpf a ser validado: ')
#
# cpf_lista = cpf_raw.split('.')[0:3]
#
# cpf_digit = ''.join(cpf_lista)
# cpf_nodigit = cpf_digit.split('-')[0]

from random import randint

numero = randint(100000000, 999999999)
cpf = str(numero)

soma_digito1 = 0
soma_digito2 = 0

for indice, valor in enumerate(range(10, 1, -1)):
    soma_digito1 += int(cpf[indice]) * valor

calculo_digito1 = 11 - (soma_digito1 % 11)
digito1 = calculo_digito1 if calculo_digito1 <= 9 else 0

cpf += str(digito1)

for indice, valor in enumerate(range(11, 1, -1)):
    soma_digito2 += int(cpf[indice]) * valor

calculo_digito2 = 11 - (soma_digito2 % 11)
digito2 = calculo_digito2 if calculo_digito2 <= 9 else 0
cpf += str(digito2)

# Evitar sequencias de numeros repetidos
sequencia = cpf == cpf[0] * 11

if cpf and not sequencia:
    print(f'CPF: {cpf}')
else:
    print('O cpf gerado foi invalidado')
