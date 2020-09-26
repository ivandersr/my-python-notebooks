from itertools import product

pessoas = ['João', 'Maria', 'José']

for grupo in product(pessoas, repeat=2):
    print(grupo)

# ('João', 'João')
# ('João', 'Maria')
# ('João', 'José')
# ('Maria', 'João')
# ('Maria', 'Maria')
# ('Maria', 'José')
# ('José', 'João')
# ('José', 'Maria')
# ('José', 'José')


