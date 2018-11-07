print('''\n17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
não bissexto.''')

print('-=-' * 21)
ano = int(input('\nInforme o ano que deseja analisar: '))

if (ano % 4 == 0) and (ano % 100 != 0) and (ano % 400 != 0):
    print('\nO ano de {} é \033[34mBISSEXTO\033[m!'.format(ano))
else:
    print('\nO ano de {} \033[33mNÃO é BISSEXTO\033[m \n' .format(ano))

print('-=-' * 21)
