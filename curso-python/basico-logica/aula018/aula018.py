contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador, sep='/', end=' - ')
    acumulador += contador
    contador += 1
    if acumulador == 22:
        break
else:
    print('Cheguei no else')
