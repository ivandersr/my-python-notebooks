class DeuRuimError(Exception):
    pass


def testar():
    raise DeuRuimError('Você conseguiu')


try:
    testar()
except DeuRuimError as err:
    print(f'Deu ruim: {err}')
