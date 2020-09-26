from datetime import date

nome = 'Ivander'
idade = 29
altura = 1.78
peso = 90.5
ano_atual = date.today().year
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'Nome: {nome} \nIdade: {idade} \nAltura: {altura} \nPeso: {peso} \nAno atual'
      f': {ano_atual} \nAno de nascimento: {ano_nascimento} \nImc: {imc:.2f}')
