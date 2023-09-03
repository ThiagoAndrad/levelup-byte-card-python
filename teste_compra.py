from model import Compra, Cartao, CompraCredito
from datetime import datetime, date

visa = Cartao('1111 1111 1111 1111', date(2031, 1, 31), '321', 1000.0, 'Steve Rogers')

compra_farmacia = Compra(100.0, datetime(2023, 1, 1, 10, 0, 0), 'Farmácia Popular', 'Saúde', visa)
compra_restaurante = Compra(89.9, datetime(2023, 1, 2, 12, 15, 0), 'Burguer King', 'Lazer', visa)
compra_supermercado = Compra(475.5, datetime(2023, 2, 3, 7, 5, 5), 'Carrefour', 'Alimentação', visa)

print(compra_farmacia)
print(compra_restaurante)
print(compra_supermercado)
print()

compra_amazon = CompraCredito(1000.0, datetime(2023, 2, 15, 19, 46, 17), 'Amazon', 'Casa', visa, 10)
print(f'Compra a crédito: {compra_amazon.valor} em {compra_amazon.quantidade_parcelas}x de {compra_amazon.valor_parcela}')
print()

fatura = [compra_farmacia, compra_restaurante, compra_supermercado, compra_amazon]
total = 0
for compra in fatura:
    total += compra.valor

print(f'O total da fatura é: {total}')
