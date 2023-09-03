from datetime import date
from model import Cartao

visa = Cartao('1111 1111 1111 1111', date(2023, 1, 31), '321', 1000.0, 'Steve Rogers')
mastercard = Cartao('2222 2222 2222 2222', '05/2035', '789', 2000.0, 'Matt Murdock')


print(visa.numero)
print(visa.validade)
print(visa.cvv)
print(visa.limite)
print(visa.cliente)
print(visa.status)

print()

print(mastercard.numero)
print(mastercard.validade)
print(mastercard.cvv)
print(mastercard.limite)
print(mastercard.cliente)
print(mastercard.status)

print()

visa.cancela()
mastercard.cancela()

print(visa.status)
print(mastercard.status)

print()

visa.limite = 5000.0
mastercard.limite = 7500.0

print(visa.limite)
print(mastercard.limite)
print()

cartao_invalido = Cartao('3333 3333 3333 3333', date(2029, 5, 31), '887', 10000.0, 'Bruce Wayne')