from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: str, conta: str, saldo=0.0):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @property
    def agencia(self) -> str:
        return self.__agencia

    @property
    def conta(self) -> str:
        return self.__conta

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        self.__saldo = valor

    def depositar(self, quantidade: (int, float)) -> None:
        if not isinstance(quantidade, (int, float)):
            raise TypeError('Quantia de depósito deve ser numérica')
        self.__saldo += quantidade

    @abstractmethod
    def sacar(self, valor: (int, float)) -> None:
        pass
