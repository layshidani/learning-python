#Faça um programa que pergunte o preço de três produtos e informe
# qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = str(input('Insira o nome do produto: '))
preco1 = float(input('Insira o preço deste produto R$ '))

prod2 = str(input('Insira o nome do produto: '))
preco2 = float(input('Insira o preço deste produto R$ '))

prod3 = str(input('Insira o nome do produto: '))
preco3 = float(input('Insira o preço deste produto R$ '))


if preco1 < preco2 and preco1 < preco3:
    print('O produto {} é o mais barato! (R$ {:.2f})' .format(prod1, preco1))
elif preco2 < preco1 and preco2 < preco3:
    print('O produto {} é o mais barato! (R${:.2f})'.format(prod2, preco2))
elif preco3 < preco1 and preco3 < preco2:
    print('O produto {} é o mais barato! (R$ {:.2f})'.format(prod3, preco3))
elif preco1 == preco2 and preco1 < preco3 and preco2 < preco3:
    print('Os produtos {} e {} são os mais baratos! (R$ {:.2f})'.format(prod1, prod2, preco1))
elif preco1 == preco3 and preco1 < preco2 and preco3 < preco2:
    print('Os produtos {} e {} são os mais baratos! (R$ {:.2f})'.format(prod1, prod3, preco1))
elif preco2 == preco3 and preco2 < preco1 and preco3 < preco1:
    print('Os produtos {} e {} são os mais baratos! (R$ {:.2f})'.format(prod2, prod3, preco2))
else:
    print('??? Fiquei confuso!')