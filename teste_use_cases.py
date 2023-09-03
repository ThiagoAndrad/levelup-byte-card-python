import use_cases

todos_os_cartoes = use_cases.lista_cartoes()
print(f'Cartões pré-cadastrados: {len(todos_os_cartoes)}')

cartao_existente = use_cases.pesquisa_cartao_por_id(1)
cartao_inexistente = use_cases.pesquisa_cartao_por_id(1000)

print(f'Cartão existente: {cartao_existente}')
print(f'Cartão existente: {cartao_inexistente}')

use_cases.cadastra_cartao('Diana Prince', 5500.0)
for cartao in use_cases.lista_cartoes():
    print(cartao)