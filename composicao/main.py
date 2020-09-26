from classes import Cliente

cliente1 = Cliente('Ivander', 29)
cliente1.insere_endereco('Maringá', 'PR')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Maria', 25)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Angra dos Reis', 'RJ')
cliente2.lista_enderecos()
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 55)
cliente3.insere_endereco('Curitiba', 'PR')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
print('_____________________')


# Ivander
# Maringá PR
#
# Salvador BA
# Angra dos Reis RJ
# Maria
# Salvador BA
# Angra dos Reis RJ
#
# João
# Curitiba PR
#
# _____________________
# Ivander foi apagado
# Maringá, PR foi apagado
# Maria foi apagado
# Angra dos Reis, RJ foi apagado
# Salvador, BA foi apagado
# João foi apagado
# Curitiba, PR foi apagado