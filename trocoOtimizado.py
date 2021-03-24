print("Troco Otimizado")
print("--" * 17)

valor = float(input('Valor da conta: '))
pago = float(input('Valor pago: '))
while pago < valor:
    pago = float(input('Valor pago(Digite um valor pago igual ou maior ao da conta): '))
print("--" * 17)

troco = pago - valor
print('O troco é {}'.format(troco))
print("--" * 17)

notaMoeda = 0
while troco >= 50:
    troco -= 50
    notaMoeda += 1
print('O número de notas/moedas de R$ 50,00: {}'.format(notaMoeda))

notaMoeda = 0
while troco >= 20:
    troco -= 20
    notaMoeda += 1
print('O número de notas/moedas de R$ 20,00: {}'.format(notaMoeda))

notaMoeda = 0
while troco >= 10:
    troco -= 10
    notaMoeda += 1
print('O número de notas/moedas de R$ 10,00: {}'.format(notaMoeda))

notaMoeda = 0
while troco >= 5:
    troco -= 5
    notaMoeda += 1
print('O número de notas/moedas de R$ 5,00: {}'.format(notaMoeda))

notaMoeda = 0
while troco >= 2:
    troco -= 2
    notaMoeda += 1
print('O número de notas/moedas de R$ 2,00: {}'.format(notaMoeda))

notaMoeda = 0
while troco >= 1:
    troco -= 1
    notaMoeda += 1
print('O número de notas/moedas de R$ 1,00: {}'.format(notaMoeda))

notaMoeda = 0
while troco >= 0.50:
    troco -= 0.50
    notaMoeda += 1
print('O número de notas/moedas de R$ 0,50: {}'.format(notaMoeda))

notaMoeda = 0
while troco >= 0.25:
    troco -= 0.25
    notaMoeda += 1
print('O número de notas/moedas de R$ 0,25: {}'.format(notaMoeda))

notaMoeda = 0
while troco >= 0.10:
    troco -= 0.10
    notaMoeda += 1
print('O número de notas/moedas de R$ 0,10: {}'.format(notaMoeda))

notaMoeda = 0

while troco >= 0.05:
    troco -= 0.05
    notaMoeda += 1
print('O número de notas/moedas de R$ 0,05: {}'.format(notaMoeda))


