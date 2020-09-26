import os
import shutil

# shutil.move(origem, destino) -> Mover o arquivo de um caminho para outro. Se for no mesmo caminho,
# pode ser utilizado para renomear
# shutil.copy(origem, destino) -> Copia o arquivo de um caminho para outro.
# os.remove(caminho) -> Exclui arquivos

caminho_raiz = '/home/ivander/workspaces/python/oslibshutil'
caminho_existente = f'{caminho_raiz}/pasta'
caminho_novo = f'{caminho_raiz}/nova_pasta'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        new_filepath = os.path.join(caminho_novo, file)

        if '.txt' in file:
            os.remove(new_filepath)
