class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.nome_classe = self.__class__.__name__

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    def falar(self):
        print(f'{self.nome_classe} está falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} está comprando')

    def falar(self):
        print(f'Método sobreposto na classe CLIENTE')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, plano):
        Pessoa.__init__(self, nome, idade)
        self.__plano = plano
