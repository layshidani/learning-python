print('''11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
\n#a. o produto do dobro do primeiro com metade do segundo .
#b. a soma do triplo do primeiro com o terceiro.
#c. o terceiro elevado ao cubo''')

Z = int(input('\nInsira um nº inteiro Z (..., -2, -1, 0, 1, 2, ...): '))
Z2 = int(input('Insira mais um nº inteiro Z (..., -2, -1, 0, 1, 2, ...): '))
R = float(input('Insira um nº real R (com parte fracionária, ex: 0.12, 2.25, etc): '))

a = (Z * 2) * ((1 / 2) * Z2)
b = Z * 3 + R
c = R ** 3

print('\na. o produto do dobro do primeiro com metade do segundo: {:.2f} ' .format(a))
print('b. a soma do triplo do primeiro com o terceiro: {:.2f}' .format(b))
print(('c. o terceiro elevado ao cubo: {:.2f}' .format(c)))
