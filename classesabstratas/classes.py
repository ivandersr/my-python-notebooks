from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo deve ser numérico')

        self.__saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor deve ser numérico')
        saldo = self.saldo + valor
        self.saldo += saldo
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass

    def detalhes(self):
        print(f'Agência: {self.agencia}')
        print(f'Conta: {self.conta}')
        print(f'Saldo: {self.saldo}')
        print()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            raise ValueError('Saldo insuficiente')
        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            raise ValueError('Saldo insuficiente')
        self.saldo -= valor
        self.detalhes()
