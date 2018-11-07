from datetime import date

print('\nExercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.')

print('-=-' * 21)
ano = int(input('\nInforme o ano que deseja analisar (digite 1 para o ano atual): '))

if ano == 1:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 != 0) and (ano % 400 != 0):
    print('\nO ano de {} é \033[34mBISSEXTO\033[m!'.format(ano))
else:
    print('\nO ano de {} \033[33mNÃO é BISSEXTO\033[m \n' .format(ano))

print('-=-' * 21)
