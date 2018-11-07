# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a. Álcool:
# b. até 20 litros, desconto de 3% por litro
# c. acima de 20 litros, desconto de 5% por litro
# d. Gasolina:
# e. até 20 litros, desconto de 4% por litro
# f. acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
# combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

print('===' * 21)
print('>>>AUTOPOSTO SP<<<')

print('\nÁlcool: R$ 1.90.\n>SUPERPROMOÇÃO!<\nAté 20 litros: desconto de 3%\nAcima de 20 litros: desconto de 5%')
print('\n\nGasolina: R$ 2.50.\n>SUPERPROMOÇÃO!<\nAté 20 litros: desconto de 4%\nAcima de 20 litros: desconto de 6%')

print('\nCalcular desconto:')

combustivel = str(input('\nInforme o tipo de combustível (G/A)\nG - Gasolina ou A - Alcool: ').upper())
litros = float(input('\nInforme a quantidade de litros: '))

if combustivel == 'A':
    if litros <= 20:
        preco_sem = litros * 1.90
        desconto = preco_sem * 0.03
        preco = preco_sem - desconto
    elif litros > 20:
        preco_sem = litros * 1.90
        desconto = preco_sem * 0.05
        preco = preco_sem - desconto

elif combustivel == 'G':
    if litros <= 20:
        preco_sem = litros * 2.50
        desconto = preco_sem * 0.04
        preco = preco_sem - desconto
    elif litros > 20:
        preco_sem = litros * 2.50
        desconto = preco_sem * 0.06
        preco = preco_sem - desconto

print('\nCombustível: {}, {} litros' .format(combustivel, litros))
print('Preço sem desconto: R$ {:.2f}'.format(preco_sem))
print('Desconto: R$ {:.2f}' .format(desconto))
print('\nPreço a pagar (COM DESCONTO) R$ {:.2f}' .format(preco))
print('===' * 21)
