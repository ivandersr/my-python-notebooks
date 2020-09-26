from itertools import groupby, tee

alunos = [
    {'nome': 'Ivander', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Letícia', 'nota': 'C'},
    {'nome': 'Natália', 'nota': 'A'},
    {'nome': 'Fernando', 'nota': 'D'},
    {'nome': 'Roseli', 'nota': 'E'},
    {'nome': 'Fernanda', 'nota': 'A'},
    {'nome': 'Carolina', 'nota': 'B'},
    {'nome': 'Jonas', 'nota': 'A'},
]

alunos.sort(key=lambda item: item['nota'])

alunos_agrupados = groupby(alunos, lambda item: item['nota'])

for agrupamento, valores in alunos_agrupados:
    print(agrupamento, end=': ')
    valores_1, valores_2 = tee(valores)
    for aluno in valores_1:
        print(aluno.get('nome'), end=', ')
    numero_alunos = len(list(valores_2))
    print()
    print(f'\tO número de alunos com nota {agrupamento} é {numero_alunos}')
    print()

# A: Ivander, Natália, Fernanda, Jonas,
# 	O número de alunos com nota A é 4
#
# B: João, Carolina,
# 	O número de alunos com nota B é 2
#
# C: Letícia,
# 	O número de alunos com nota C é 1
#
# D: Fernando,
# 	O número de alunos com nota D é 1
#
# E: Roseli,
# 	O número de alunos com nota E é 1



