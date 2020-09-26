frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_frase = ''

letra_maiuscula = input('Qual letra você deseja que fique maiúscula? ').lower()

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == letra_maiuscula:
        nova_frase += letra_maiuscula.upper()
    else:
        nova_frase += letra
    contador += 1

print(nova_frase)
