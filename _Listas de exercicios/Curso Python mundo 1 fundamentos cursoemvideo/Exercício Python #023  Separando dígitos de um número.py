print('''Exercício Python 023: Faça um programa que leia um número de 0 a 9999 
e mostre na tela cada um dos dígitos separados.''')

n = int(input('\nInforme um nº: '))

unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10

print('\nAo analisar o nº {}' .format(n))
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
         ''' .format(unidade, dezena, centena, milhar))