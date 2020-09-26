# lista = ['A', 'B', 'Cacilds', 'D', 'E']
#
# print(lista[:])
# print(lista[::])
# print(lista[:4])
# print(lista[3:])
# print(lista[::2])
# print(lista[::-1])

# lista = list(range(0, 100, 9))
#
# soma = 0
# for valor in lista:
#     soma += valor
# print(f'Soma dos valores da lista: {soma}')
#
# l1 = ['String', True, 10, -20.5]
#
# for elemento in l1:
#     print(f'O tipo de {elemento} é {type(elemento)}')
#

palavra = 'cachorro'
digitadas = []
vidas = 3

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in palavra:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta', end=' - ')
        digitadas.pop()
        vidas -= 1
        if vidas > 0:
            print(f'Você ainda tem {vidas} vida(s)!')
        else:
            print(f'Suas vidas acabaram. Fim de jogo.')
            break

    palavra_temp = ''
    for letra_certa in palavra:
        if letra_certa in digitadas:
            palavra_temp += letra_certa
        else:
            palavra_temp += '*'

    if palavra_temp == palavra:
        print(f'Ganhou! A palavra secreta era "{palavra_temp}"')
        break
    else:
        print(f'Palavra secreta: {palavra_temp}')

