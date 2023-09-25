from datetime import datetime, date

from model import CompraCredito, Cartao


class TestCompraCredito:

    def test_valor_deve_ser_acrescido_de_taxa(self):
        valor_compra = 1000.00
        visa = Cartao('1111 1111 1111 1111', date(2031, 1, 31), '321', 1000.0, 'Steve Rogers')
        compra = CompraCredito(valor_compra, datetime(2023, 2, 15, 19, 46, 17), 'Amazon', 'Casa', visa, 10)

        valor_com_taxa = compra.valor

        assert valor_com_taxa == 1100.00

    def test_quando_compra_for_parcelada_valor_das_parcelas_deve_ser_dividido_igualmente(self):
        valor_compra = 1000.00
        quantidade_de_parcelas = 10
        visa = Cartao('1111 1111 1111 1111', date(2031, 1, 31), '321', 1000.0, 'Steve Rogers')
        compra = CompraCredito(valor_compra, datetime(2023, 2, 15, 19, 46, 17), 'Amazon', 'Casa', visa, quantidade_de_parcelas)

        valor_parcela = compra.valor_parcela

        assert valor_parcela == 110.00
