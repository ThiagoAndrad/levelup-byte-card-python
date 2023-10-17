from excecoes import ValorExcedidoException


class Cartao:

    def __init__(self, numero, validade, cvv, limite, cliente, id=None):
        self.__numero = numero
        self.__validade = validade
        self.__cvv = cvv
        self.__set__limite(limite)
        self.__set_cliente(cliente)
        self.__status = 'ATIVO'
        self.__id = id

    def cancela(self):
        self.__status = 'CANCELADO'

    def ativa(self):
        self.__status = 'ATIVO'

    @property
    def is_ativo(self):
        return self.status == 'ATIVO'

    @property
    def is_cancelado(self):
        return self.status == 'CANCELADO'

    @property
    def id(self):
        return self.__id

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

    @limite.setter
    def limite(self, limite):
        self.__set__limite(limite)

    def __set__limite(self, limite):
        limite_minimo = 10
        if limite < limite_minimo:
            raise ValueError(f'O limite deve ser de no mínimo {limite_minimo}')
        self.__limite = limite

    @property
    def cliente(self):
        return self.__cliente

    @property
    def status(self):
        return self.__status

    def __set_cliente(self, cliente):
        if cliente is None:
            raise ValueError('Cliente é obrigatório')
        if len(cliente) < 2:
            raise ValueError('Cliente com caracteres insuficientes')
        nomes = cliente.split()
        if len(nomes) < 2:
            raise ValueError('Cliente deve ter nome e sobrenome')
        self.__cliente = cliente

    def __str__(self):
        return f'Cartão(#{self.id}) {self.numero} do(a) {self.cliente} com limite de {self.limite} válido até {self.validade}'


class Compra:

    def __init__(self, valor, data, estabelecimento, categoria, cartao, id=None):
        self.__set__valor(valor)
        self.__data = data
        self.__set__estabelecimento(estabelecimento)
        self.__categoria = categoria.strip()
        self.__set__cartao(cartao)
        self.__id = id
        self.valida_compra()

    @property
    def valor(self):
        return self.__valor

    @property
    def categoria(self):
        return self.__categoria

    def __set__valor(self, valor):
        if valor <= 0:
            raise ValueError(f"O valor {valor} deve ser superior a zero")
        self.__valor = valor

    def __set__cartao(self, cartao):
        if cartao is None:
            raise ValueError("É obrigatório um cartão")
        self.__cartao = cartao

    def __set__estabelecimento(self, estabelecimento):
        limite_caracteres = 30
        tamanho_estabelecimento = len(estabelecimento)
        if tamanho_estabelecimento > limite_caracteres:
            raise ValueError(
                f'Estabelecimento com {tamanho_estabelecimento} caracteres é superior ao limite de {limite_caracteres} caracteres')
        self.__estabelecimento = estabelecimento.strip()

    def valida_compra(self):
        limite = self.__cartao.limite
        valor = self.__valor
        if valor > limite:
            valor_excedido = valor - limite
            raise ValorExcedidoException(f'O valor da compra excedeu ${valor_excedido} do limite')

    def __str__(self):
        return f'Compra: {self.__valor} no dia {self.__data} em {self.__estabelecimento} no cartão {self.__cartao.numero}'


class CompraCredito(Compra):

    def __init__(self, valor, data, estabelecimento, categoria, cartao, quantidade_parcelas=1, id=None):
        super().__init__(valor, data, estabelecimento, categoria, cartao, id)
        self.__quantidade_parcelas = quantidade_parcelas

    @property
    def valor(self):
        return super().valor * 1.1

    @property
    def quantidade_parcelas(self):
        return self.__quantidade_parcelas

    @property
    def valor_parcela(self):
        return self.valor / self.quantidade_parcelas
