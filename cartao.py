class Cartao:
    def __init__(self, numero, validade, cvv, limite, cliente):
        self.cliente = cliente
        self.limite = limite
        self.cvv = cvv
        self.validade = validade
        self.numero = numero
        self.status = 'ATIVO'

    def cancela(self):
        self.status = 'CANCELADO'

    def ativa(self):
        self.status = 'ATIVO'