print('>>>HIPERMERCADOS TABAJARA<<<')
print('\nHiperPROMOÇÕES para você!!!')
print('\nSemana da CARNE...Confira:\n*Válido apenas para um tipo de carne por cliente.')

print('\nAté 5 kg:\n'
      'Filé duplo: R$ 5.80 kg \n'
      'Alcatra: R$ 6.80 kg\n'
      'Picanha: R$ 7.80 kg\n')
print('Acima de 5 kg:\n'
      'Filé duplo: R$ 4.90 kg \n'
      'Alcatra: R$ 5.90 kg\n'
      'Picanha: R$ 6.90 kg\n')
print('\n>>>E tem MAIS....'
      '\nCliente que comprar usando o CARTÃO Tabajara...'
      '\n desconto de mais 5% sobre o total!!!<<<')
print('\n>>>CALCULAR DESCONTO<<<')

forma_de_pagamento = str(input('''Informe a forma de pagamento: 
D - Dinheiro
C - Cartão comum 
T - Cartão TABAJARA''').upper())

carne = str(input('''\nInforme o tipo de carne:
F - Filé duplo
A - Alcatra
P - Picanha''').upper())

kilo = float(input('\nInforme a quantidade: kg '))

if carne == 'F':
    if kilo <= 5:
        preco_carne = kilo * 5.80
    elif kilo > 5:
        preco_carne = kilo * 4.90
elif carne == 'A':
    if kilo <= 5:
        preco_carne = kilo * 6.80
    elif kilo > 5:
        preco_carne = kilo * 5.90
elif carne == 'P':
    if kilo <= 5:
        preco_carne = kilo * 7.80
    elif kilo > 5:
        preco_carne = kilo * 6.90

print('\n>>>RESUMO DA COMPRA<<<')
if carne == 'F':
    print('\nTipo de carne: Filé duplo\nQuantidade: {:.2f} kg' .format(kilo))
elif carne == 'A':
    print('\nTipo de carne: Alcatra\nQuantidade: {:.2f} kg' .format(kilo))
else:
    print('\nTipo de carne: Picanha\nQuantidade: {:.2f} kg' .format(kilo))

if forma_de_pagamento == 'T':
    desconto = preco_carne * 0.05
    preco_final = preco_carne - desconto
elif forma_de_pagamento == 'D' or forma_de_pagamento == 'C':
    preco_final = preco_carne

if preco_final < preco_carne:
    print('\nForma de pagamento: CARTÃO TABAJARA\n:D Cliente TABAJARA detectado!.....mais 5% de desconto!')
    print('Valor do desconto: R$ {:.2f}' .format(desconto))
    print('\nTotal a pagar: R$ {:.2f}' .format(preco_final))
else:
    print('\nForma de pagamento: {} :/ que pena.. o cliente não ganhou 5% de desconto' .format(forma_de_pagamento))
    print('Valor do desconto: R$ 0.00')
    print('\nTotal a pagar: R$ {:.2f}'.format(preco_final))




