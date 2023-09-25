import use_cases

todos_os_cartoes = use_cases.lista_cartoes()
print(f'Cartões pré-cadastrados: {len(todos_os_cartoes)}')

try:
    use_cases.cadastra_compra(1, 100.0, 'Joalheria', 'Joalheria Jóias do Infinito by Thanos')
except Exception as e:
    print(e)

try:
    use_cases.cadastra_compra(1, 0, 'Alimentação', 'Pizza Dois Pedaços')
except Exception as e:
    print(e)

try:
    use_cases.cadastra_compra(None, 100.0, 'Alimentação', 'Pizza Dois Pedaços')
except Exception as e:
    print(e)

try:
    use_cases.cadastra_compra(1, 50_000.0, 'Alimentação', 'Pizza Dois Pedaços')
except Exception as e:
    print(e)

for compra in use_cases.lista_compras():
    print(compra)

try:
    use_cases.cadastra_cartao('Peter Parker', 9)
except Exception as e:
    print(e)

try:
    use_cases.cadastra_cartao('Peter', 10)
except Exception as e:
    print(e)

try:
    use_cases.cadastra_cartao(None, 10)
except Exception as e:
    print(e)

try:
    use_cases.cadastra_cartao("P", 10)
except Exception as e:
    print(e)