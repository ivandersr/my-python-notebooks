# num1 = 1
# num2 = 2
# expressao_igual = num1 == num2
# expressao_maior = num1 > num2
# expressao_diferente = num1 != num2
#
# print(f'Os números são iguais: {expressao_igual}')
# print(f'O primeiro número é maior que o segundo: {expressao_maior}')
# print(f'Os números são diferentes: {expressao_diferente}')

nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))
idade_minima = 20  # Idade mínima para obter um empréstimo
idade_maxima = 30  # Idade máxima para obter um empréstimo

if idade >= idade_minima and idade <= idade_maxima:
    print(f'{nome} pode receber o empréstimo')
else:
    print(f'{nome} está fora da faixa de idade para receber o empréstimo')




