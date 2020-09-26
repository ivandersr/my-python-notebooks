from itertools import count

contador = count(start=10, step=-2.5)

for valor in contador:
    print(f'{valor:.1f}')

    if valor <= 0:
        break
