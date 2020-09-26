def func(*args, **kwargs):
    print(args)
    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    if idade:
        print(nome, idade)
    else:
        print(nome, 'Idade não informada')


func(1, 2, 3, 4, 5, nome='Ivander', sobrenome='Salvador')
# (1, 2, 3, 4, 5)
# {'nome': 'Ivander', 'sobrenome': 'Salvador'}
# Ivander