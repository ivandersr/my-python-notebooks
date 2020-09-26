from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Leialo')
caneta = Caneta('Vermelha')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta

escritor.ferramenta.escrever()

del escritor
maquina.escrever()
print(escritor)