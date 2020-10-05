from time import sleep
from threading import Thread, Lock


# Opção 1
# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo
#         super().__init__()
#
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)
#
#
# t1 = MeuThread('Thread 1', 2)
# t1.start()
#
# t2 = MeuThread('Thread 2', 1)
# t2.start()
#
# t3 = MeuThread('Thread 3', 8)
# t3.start()
#
# for i in range(10):
#     print(i)
#     sleep(1)

# Opção 2
# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)
#
#
# t1 = Thread(target=vai_demorar, args=('Olá 1', 10))
# t1.start()
# t1.join()  # Thread volta a ser blocking (se une à main thread)

# while t1.is_alive():
#     print('Esperando a thread.')
#     sleep(2)

# print('Thread acabou')

# t2 = Thread(target=vai_demorar, args=('Olá 2', 3))
# t2.start()
#
# t3 = Thread(target=vai_demorar, args=('Olá 3', 8))
# t3.start()
#
# for i in range(10):
#     print(i)
#     sleep(1)

# Manipulação de dados pode sofrer com assincronia quando se trabalha com threads
class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()  # Trava o método para o acesso de apenas uma thread por vez
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            self.lock.release()  # Libera o acesso
            return
        sleep(1)  # Caso haja assincronia, todas as threads passaram pela verificação anterior
        self.estoque -= quantidade  # Todas as threads reduzirão o estoque, sem controle de estoque
        print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque}.')

        self.lock.release()  # Libera o acesso


if __name__ == '__main__':
    ingresso = Ingresso(12)
    threads = []

    for i in range(10):
        t = Thread(target=ingresso.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    executando = True

    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingresso.estoque)
