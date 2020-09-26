# texto = 'o rato roeu a roupa do rei de roma'
#
# for letra in texto:
#     print(letra, end='_')
#
# for numero in range(20, 10, -1):
#     print(numero, end='-')

# for numero in range(0, 100, 15):
#     print(numero, end='/')
#
# print()
#
# for numero in range(100):
#     if numero % 15 == 0:
#         print(numero, end='/')

texto = 'o rato roeu a roupa do rei de roma'
novo_texto = ''

for letra in texto:
    if letra == 't' or letra == 'o':
        continue
    elif letra == 'm':
        break
    else:
        novo_texto += letra

print(novo_texto)


