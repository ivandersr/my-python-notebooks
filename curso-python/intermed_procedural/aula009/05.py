lista = [1, 2, 3, 4, 5, 6]
#
# iterador = iter(lista)
#
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
#
# print('A partir daqui, o loop for inicia')
# for v in iterador:
#     print(v)
#
# print('Segundo loop for inicia')
# for v in iterador:
#     print(v)
# # 1
# # 2
# # 3
# # 4
# # A partir daqui, o loop for inicia
# # 5
# # 6
# # Segundo loop for inicia

gerador = (v for v in range(1, 7))

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('Primeiro loop for')
for v in gerador:
    print(v)

print('Segundo loop for')
for v in gerador:
    print(v)
# 1
# 2
# 3
# 4
# Primeiro loop for
# 5
# 6
# Segundo loop for