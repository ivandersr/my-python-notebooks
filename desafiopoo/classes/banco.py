from typing import List
from classes.conta import Conta
from classes.cliente import Cliente


class Banco:
    def __init__(self):
        self.__contas: List[Conta] = []
        self.__clientes: List[Cliente] = []

    @property
    def contas(self) -> List[Conta]:
        return self.__contas

    @property
    def clientes(self) -> List[Cliente]:
        return self.__clientes

    def registrar_conta(self, conta: Conta):
        self.__contas.append(conta)

    def autenticar_conta(self, conta: Conta):
        return conta in self.__contas

    def registrar_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)
        self.registrar_conta(cliente.conta)

    def autenticar_cliente(self, cliente: Cliente):
        return cliente in self.__clientes
