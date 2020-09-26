import re


class CalcIPv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo
        self._set_broadcast()
        self._set_rede()

    @property
    def ip(self):
        return self.__ip

    @property
    def mascara(self):
        return self.__mascara

    @property
    def prefixo(self):
        return self.__prefixo

    @property
    def rede(self):
        return self.__rede

    @property
    def broadcast(self):
        return self.__broadcast

    @property
    def num_ips(self):
        return self._get_numero_ips()

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('IP inválido')
        self.__ip = valor
        self.__ip_bin = self._ip_to_bin(valor)

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return
        if not self._valida_ip(valor):
            raise ValueError('Máscara inválida')
        self.__mascara = valor
        self.__mascara_bin = self._ip_to_bin(valor)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self.__mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return

        if not isinstance(valor, int):
            raise TypeError('Prefixo deve ser inteiro')

        if not valor >= 0 and valor <= 32:
            raise ValueError('Prefixo inválido')

        self.__prefixo = valor
        self.__mascara_bin = (valor * '1').ljust(32, '0')

        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self.__mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        regex = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        return regex.search(ip)

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_bin = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_bin)

    @staticmethod
    def _bin_to_ip(ip):
        bloco_len = 8
        blocos = [str(int(ip[i:bloco_len + i], 2)) for i in range(0, 32, bloco_len)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self.__broadcast_bin = (self.__ip_bin[:self.prefixo] + (host_bits * '1'))
        self.__broadcast = self._bin_to_ip(self.__broadcast_bin)
        return self.__broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self.__rede_bin = (self.__ip_bin[:self.prefixo] + (host_bits * '0'))
        self.__rede = self._bin_to_ip(self.__rede_bin)
        return self.__rede

    def _get_numero_ips(self):
        return 2 ** (32 - self.prefixo)
