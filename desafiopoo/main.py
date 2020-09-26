from classes.banco import Banco
from classes.cliente import Cliente
from classes.contacorrente import ContaCorrente
from classes.contapoupanca import ContaPoupanca

banco = Banco()

cliente1 = Cliente('Ivander', 29)
cliente1.abrir_conta(ContaCorrente('2207-1', '7445-4', 500))
banco.registrar_cliente(cliente1)

print(banco.autenticar_cliente(cliente1))
print(banco.autenticar_conta(cliente1.conta))

cliente1.conta.sacar(300)
cliente1.conta.sacar(300)

cliente2 = Cliente('Pamela', 26)
cliente2.abrir_conta(ContaPoupanca('1151-1', '55621-1'))

cliente2.conta.sacar(10)
cliente2.conta.depositar(50)
cliente2.conta.sacar(10)
