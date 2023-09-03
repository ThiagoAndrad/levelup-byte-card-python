from datetime import date

from model import Cartao, cria_numero_do_cartao, cria_cvv_do_cartao, define_validade_do_cartao

cartao1 = Cartao(cria_numero_do_cartao(), date(2031, 1, 31), '321', 1000.0, 'Steve Rogers', id=1)
cartao2 = Cartao(cria_numero_do_cartao(), date(2035, 5, 31), '789', 2000.0, 'Matt Murdock', id=2)
cartao3 = Cartao(cria_numero_do_cartao(), date(2029, 5, 31), '887', 10000.0, 'Bruce Wayne', id=3)

banco_cartoes = [cartao1, cartao2, cartao3]
sequencia_ids = 4


def lista_cartoes():
    return banco_cartoes


def pesquisa_cartao_por_id(id):
    for cartao in banco_cartoes:
        if cartao.id == id:
            return cartao


def cadastra_cartao(cliente, limite):
    global sequencia_ids, banco_cartoes

    numero = cria_numero_do_cartao()
    cvv = cria_cvv_do_cartao()
    validade = define_validade_do_cartao()

    novo_cartao = Cartao(numero=numero, validade=validade, cvv=cvv, limite=limite, cliente=cliente, id=sequencia_ids)
    banco_cartoes.append(novo_cartao)

    sequencia_ids += 1
