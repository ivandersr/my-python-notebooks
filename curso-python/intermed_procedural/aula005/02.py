import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 4: [1, 2, 3]}

variavel = copy.deepcopy(d1)  # cópia profunda de d1

variavel.update({1: 'novo, valor'})
variavel.get(4)[0] = 5

print(d1)
print(variavel)
