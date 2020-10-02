import sys
import os

'''
Retorna uma lista, na qual o primeiro argumento é o arquivo executado e o restante 
são argumentos seguintes na execução em terminal
'''

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltando argumentos:')
    print('-a', 'Para listar todos os arquivos desta pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios desta pasta', sep='\t')
    sys.exit()

so_arquivos = False
so_diretorios = False

if '-a' in argumentos:
    so_arquivos = True

if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)
    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)
