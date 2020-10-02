from dados import *
import json

with open('clientes.json', 'r') as file:
    clientes = json.load(file)

print(clientes)
