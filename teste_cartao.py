from cartao import Cartao

visa = Cartao('1111 1111 1111 1111', '01/2031', '321', 1000.0, 'Steve Rogers')
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
