from datetime import date

from sqlalchemy import String, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column

from database import db
from excecoes import ValorExcedidoException


class Cartao(db.Model):
    __tablename__ = "cartoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(String(30))
    cvv: Mapped[str] = mapped_column(String(3))

    limite: Mapped[float] = mapped_column(Numeric(precision=15, scale=2))
    validade: Mapped[date] = mapped_column(Date())

    cliente: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(100))

    def __init__(self, **kwargs):
        super().__init__(status='ATIVO', **kwargs)

    def cancela(self):
        self.status = 'CANCELADO'

    def ativa(self):
        self.status = 'ATIVO'

    @property
    def is_ativo(self):
        return self.status == 'ATIVO'

    @property
    def is_cancelado(self):
        return self.status == 'CANCELADO'

    def __str__(self):
        return f'Cartão(#{self.id}) {self.numero} do(a) {self.cliente} com limite de {self.limite} válido até {self.validade}'

    def __repr__(self) -> str:
        return f'Cartao(id={self.id!r}, numero={self.numero!r}, cvv={self.cvv!r}, validade={self.validade!r}, limite={self.limite!r}, cliente={self.cliente!r}, status={self.status!r})'


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
