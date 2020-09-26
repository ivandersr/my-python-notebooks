from classes.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        print(f'Saque realizado. Novo saldo: {self.saldo}')
