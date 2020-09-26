hora = input('Digite a hora atual: ')

if hora.isdecimal():
    hora = int(hora)
    if 0 <= hora < 12:
        print('Bom dia')
    elif 12 <= hora < 18:
        print('Boa tarde')
    elif 18 <= hora < 24:
        print('Boa noite')
    else:
        print('Hora inválida')
else:
    print('Por favor, digite a hora atual como número inteiro')
