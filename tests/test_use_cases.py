from use_cases import cria_numero_do_cartao, cria_cvv_do_cartao
import re


class TestUseCases:

    def test_deve_criar_cvv_cartao_numerico(self):
        cvv = cria_cvv_do_cartao()

        assert cvv.isnumeric() == True

    def test_deve_criar_cvv_cartao_de_tamanho_correto(self):
        cvv = cria_cvv_do_cartao()

        assert len(cvv) == 3

    def test_deve_criar_numero_de_cartao_no_padrao_correto(self):
        numero = cria_numero_do_cartao()

        resultado = re.match('[\d]{4} [\d]{4} [\d]{4} [\d]{4}', numero)

        assert bool(resultado) == True
