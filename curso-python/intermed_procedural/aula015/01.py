try:
    a = 1/0
except NameError as erro:
    print('Erro:', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado:', erro)
else:
    pass
finally:
    a = None

print(a)
