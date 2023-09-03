class Cartao:
    def __init__(self, numero, validade, cvv, limite, cliente):
        self.__cliente = cliente
        self.__limite = limite
        self.__cvv = cvv
        self.__validade = validade
        self.__numero = numero
        self.__status = 'ATIVO'

    @property
    def numero(self):
        return self.__numero

    @property
    def validade(self):
        return self.__validade

    @property
    def cvv(self):
        return self.__cvv

    @property
    def limite(self):
        return self.__limite

    @property
    def cliente(self):
        return self.__cliente

    @property
    def status(self):
        return self.__status

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def cancela(self):
        self.__status = 'CANCELADO'

    def ativa(self):
        self.__status = 'ATIVO'


class Compra:
    pass
