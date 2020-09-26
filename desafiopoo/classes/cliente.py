from classes.pessoa import Pessoa
from classes.conta import Conta


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.__conta = None

    def abrir_conta(self, conta: Conta):
        self.__conta = conta

    @property
    def conta(self) -> Conta:
        return self.__conta
