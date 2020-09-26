num = input('Digite um número inteiro: ')

if num.isdecimal():
    num = int(num)
    print('ímpar') if num % 2 == 1 else print('par')
else:
    print('Número não é inteiro')
