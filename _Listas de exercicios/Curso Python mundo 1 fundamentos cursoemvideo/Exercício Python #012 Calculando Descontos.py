# coding: utf-8

p = float(input('Informe o preço do produto: R$ '))
d = float(input('Agora informe o % de desconto: '))
valor_do_desconto = p * (d/100)
preco_com_desconto = p - valor_do_desconto
print('\nParabéns, você obteve um desconto de R$ {:.2f}'.format(valor_do_desconto))
print('O preço a ser pago pelo produto é R$ {:.2f}'. format(preco_com_desconto))
