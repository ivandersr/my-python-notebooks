def gerador():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel


g = gerador()

print(next(g))
print(next(g))
print(next(g))
