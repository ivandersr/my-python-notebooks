# a = 2
# b = 3
#
# if not b > a:
#     print('B é menor do que A')
# else:
#     print('A é menor ou igual a B')
#
# a = ''
# b = 0
# c = '0'
# d = 2
#
# if not a:
#     print('A está vazio')
#
# if not b:
#     print('B está vazio')
#
# if not c:
#     print('C está vazio')
#
# if not d:
#     print('D está vazio')

# if 'a' in 'Ivander':
#     print('Seu nome tem a letra A!')
#
# if 'ande' in 'Ivander':
#     print('A substring "ande" está em seu nome!')
#
# if 'u' not in 'Ivander':
#     print('Seu nome não possui a letra U!')

usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'ivander'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Usuário autenticado')
else:
    print('Combinação usuário/senha inválida')
