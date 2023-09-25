from use_cases import cria_numero_do_cartao, cria_cvv_do_cartao


class TestUseCases:

    def test_deve_criar_cvv_cartao_numerico(self):
        cvv = cria_cvv_do_cartao()

        assert cvv.isnumeric() == True

    def test_deve_criar_cvv_cartao_de_tamanho_tres(self):
        cvv = cria_cvv_do_cartao()

        assert len(cvv) == 3
