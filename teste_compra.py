from model import Compra, Cartao

visa = Cartao('1111 1111 1111 1111', '01/2031', '321', 1000.0, 'Steve Rogers')

compra_farmacia = Compra(100.0, '01/01/2023 10:00:00', 'Farmácia Popular', 'Saúde', visa)
compra_restaurante = Compra(89.9, '02/01/2023 12:15:00', 'Burguer King', 'Lazer', visa)
compra_supermercado = Compra(475.5, '03/02/2023 07:05:05', 'Carrefour', 'Alimentação', visa)

print(compra_farmacia)
print(compra_restaurante)
print(compra_supermercado)
print()
