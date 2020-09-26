from intermed_procedural.aula014.dados import produtos, pessoas, lista

nomes = map(lambda v: v.get('nome'), pessoas)

print(list(nomes))
