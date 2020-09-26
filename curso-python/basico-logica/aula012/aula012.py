# usuario = input('Digite o nome do seu usuário: ')
# qtd_caracteres = len(usuario)
#
# if qtd_caracteres < 6:
#     print('O nome do usuário deve ter ao menos 6 caracteres')
# else:
#     print('Usuário criado com sucesso!')

string1 = input('Digite o primeiro texto: ')
string2 = input('Digite o segundo texto: ')

print(f'A quantidade de caracteres total é de {len(string1) + len(string2)}')

print(string1.capitalize())
print(string1.upper())
print(string1.__len__())
