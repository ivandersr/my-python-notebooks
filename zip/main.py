from zipfile import ZipFile
import os

filepath = r'E:\\Downloads\\world'

with ZipFile('arquivo.zip', 'w') as zipzip:
    for file in os.listdir(filepath):
        complete_filepath = os.path.join(filepath, file)
        zipzip.write(complete_filepath, file)

with ZipFile('arquivo.zip', 'r') as zipzip:
    for file in zipzip.namelist():
        print(file)

with ZipFile('arquivo.zip', 'r') as zipzip:
    zipzip.extractall('descompactado')
