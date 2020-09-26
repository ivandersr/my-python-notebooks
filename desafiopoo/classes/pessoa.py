class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def idade(self) -> int:
        return self.__idade
