print('===Faça um Programa que peça dois números e imprima o maior deles===')

n1 = int(input('\n\nInsira um número inteiro qualquer: '))
n2 = int(input('Insira outro número inteiro qualquer: '))

if n1 > n2:
    print('\nO maior número é {}' .format(n1))
else:
    print('\nO maior número é {}' .format(n2))