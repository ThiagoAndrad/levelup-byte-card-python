from datetime import date, datetime

import pytest

from excecoes import ValorExcedidoException
from model import Cartao, Compra


class TestCompra:

    def test_quando_estabelecimento_for_invalido_deve_lancar_erro(self):
        with pytest.raises(ValueError):
            visa = Cartao('1111 1111 1111 1111', date(2031, 1, 31), '321', 1000.0, 'Steve Rogers')

            compra = Compra(100.0, datetime(2023, 1, 1, 10, 0, 0), 'Farmácia Popular Brasileira SA ', 'Saúde', visa)
            assert compra

    def test_quando_cartao_nao_existir_deve_lancar_erro(self):
        with pytest.raises(ValueError):

            compra = Compra(100.0, datetime(2023, 1, 1, 10, 0, 0), 'Farmácia Popular', 'Saúde', None)

            assert compra

    def test_quando_dados_sao_validos_deve_criar_compra(self):
        visa = Cartao('1111 1111 1111 1111', date(2031, 1, 31), '321', 1000.0, 'Steve Rogers')

        compra = Compra(100.0, datetime(2023, 1, 1, 10, 0, 0), 'Farmácia Popular', 'Saúde', visa)

        assert compra

    def test_quando_valor_da_compra_eh_maior_que_limite_deve_lancar_erro(self):
        with pytest.raises(ValorExcedidoException):
            visa = Cartao('1111 1111 1111 1111', date(2031, 1, 31), '321', 100.0, 'Steve Rogers')

            compra = Compra(100.01, datetime(2023, 1, 1, 10, 0, 0), 'Farmácia Popular', 'Saúde', visa)

            assert compra
