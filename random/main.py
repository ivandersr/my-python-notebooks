# coding=utf8
import random
import string

inteiro = random.randint(1, 60)  # Gera um inteiro aleatorio entre os parametros informados
inteiro2 = random.randrange(1, 61, 2)  # Gera um inteiro aleatorio dentro do range, com o passo informado
flutuante = random.uniform(1, 60)  # Gera um ponto flutuante aleatorio entre os parametros informados
flutuante2 = random.random()  # Gera um ponto flutuante aleatorio entre 0 e 1

lista = ['Candidato 1', 'Candidato 2', 'Candidato 3', 'Candidato 4', 'Candidato 5']

sorteio = random.choice(lista)  # Escolhe um elemento da lista de maneira aleatoria
sorteio2 = random.choices(lista, k=2)  # Retorna uma lista que é um fatiamento aleatorio, baseado no numero de elementos
sorteio3 = random.sample(lista, 2)  # Retorna um fatiamento aleatório da lista, sem repetições de dados
random.shuffle(lista)  # Embaralha a lista original

letras = string.ascii_letters  # Retorna uma string com todas as letras maiúsculas e minúsculas
digitos = string.digits  # Retorna uma string com todos os dígitos disponívels (0 a 9)
caracteres = '!@#$%&*._-='
caracteres_disponives = letras + digitos + caracteres

senha = ''.join(random.choices(caracteres_disponives, k=20))  # converte a lista retornada em string

# print(inteiro)
# print(inteiro2)
# print(flutuante)
# print(flutuante2)
# print(sorteio)
# print(sorteio2)
# print(sorteio3)
# print(lista)
print(senha)
