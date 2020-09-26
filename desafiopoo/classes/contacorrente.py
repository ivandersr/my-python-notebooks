from classes.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia: str, conta: str, limite: float, saldo: float = 0.0):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite

    @property
    def limite(self) -> float:
        return self.__limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        print(f'Saque realizado. Novo saldo: {self.saldo}')
