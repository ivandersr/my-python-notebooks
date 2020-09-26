class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__enderecos = []

    def insere_endereco(self, cidade, estado):
        self.__enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade, endereco.estado)

    @property
    def nome(self):
        return self.__nome

    def __del__(self):
        print(f'{self.__nome} foi apagado')


class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    def __del__(self):
        print(f'{self.cidade}, {self.estado} foi apagado')
