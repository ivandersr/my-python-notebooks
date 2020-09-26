import os
from utils import formata_tamanho

caminho_procura = input('Informe o caminho do diretório: ')
termo_procura = input('Informe o termo de procura: ')
contador = 0


for raiz, diretorio, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)

                print()
                print(f'Encontrei o arquivo: {arquivo}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {ext_arquivo}')
                print(f'Tamanho: {formata_tamanho(tamanho_arquivo)}')
            except PermissionError:
                print('Você não tem permissão para acessar este arquivo')
            except FileNotFoundError:
                print('Arquivo não encontrado')
            except Exception as err:
                print(f'Erro não esperado: {err}')

print()
print(f'{contador} arquivo(s) encontrado(s).')
