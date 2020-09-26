class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    @property
    def nome(self):
        return self._nome

    def ligar(self):
        if self._ligado:
            return
        else:
            self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        else:
            self._ligado = False


class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(F'INFO: {msg}')

    def log_error(self, msg):
        self.write(F'ERROR: {msg}')


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado'
            print(error)
            self.log_error(error)
            returnAssim
        if self._conectado:
            error = f'{self._nome} já está conectado'
            print(error)
            self.log_error(error)
            return
        self._conectado = True
        info = f'{self._nome} foi conectado'
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self._ligado:
            print(f'{self._nome} não está ligado')
            return
        if not self._conectado:
            print(f'{self._nome} não está conectado')
            return
        self._conectado = False


