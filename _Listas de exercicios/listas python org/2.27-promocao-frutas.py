print('\n>>>SUPERPROMOÇÃO DE FRUTAS!!!<<<')
print('\nAté 5 kg:\n'
      'Morango: R$ 2.50 kg \n'
      'Maçã: R$ 1.80 kg\n')
print('Acima de 5 kg:\n'
      'Morango: R$ 2.20 kg \n'
      'Maçã: R$ 1.50 kg\n')
print('\n>>>E tem MAIS....'
      '\nAcima de 8 kg ou acima de R$ 25.00 em compras...'
      '\n desconto de mais 10% sobre o total!!!<<<')
print('\n>>>CALCULAR DESCONTO<<<')

morango = float(input('\n>>>MORANGOS<<<\nInforme a quantidade (kg): '))
maca = float(input('\n>>>MAÇÃ<<<\nInforme a quantidade (kg): '))

if morango <= 5:
    preco_morango = morango * 2.50
elif morango > 5:
    preco_morango = morango * 2.20
if maca <= 5:
    preco_maca = maca * 1.80
elif maca > 5:
    preco_maca = maca * 1.50

kilo_total = morango + maca
preco_sem = preco_morango + preco_maca

if (kilo_total > 8) or (preco_sem > 25.00):
    desconto = (preco_sem * 0.10)
    preco_final = preco_sem - desconto
else:
    preco_final = preco_sem

print('\n>>>RESUMO DA COMPRA<<<')
print('Morango: {} kg'
      ' -> Preço R$ {:.2f}' .format(morango, preco_morango))
print('Maçã: {} kg'
      ' -> Preço R$ {:.2f}' .format(maca, preco_maca))
print('Total de kg: {:.2f}' .format(kilo_total))

if preco_final < preco_sem:
    print(':) Parabéns! Você ganhou desconto de 10%... Desconto = R$ {:.2f}' .format(desconto))
    print('\nPreço final: R$ {:.2f}'.format(preco_final))
else:
    print(':/ Você não ganhou o desconto de 10%...')
    print('\nPreço final: R$ {:.2f}'.format(preco_final))