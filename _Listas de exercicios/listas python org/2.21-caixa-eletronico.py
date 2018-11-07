# coding: utf-8

# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
# de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na
# máquina.
# a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de
# 5 e uma nota de 1;
# b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas
# de 10, uma nota de 5 e quatro notas de 1.

print('\n===Caixa Eletrônico==\n>>>Banco Ferraz<<<')
v_saque = float(input('\nQue valor que você deseja sacar? R$ '))

if v_saque < 10:
    print('\nTENTE NOVAMENTE. O valor mínimo para saque é R$ 10,00. Insira outro valor.')
else:
    centena = (v_saque // 100)
    cinquenta = (v_saque - (centena * 100)) // 50
    dez = (v_saque - (centena * 100) - (cinquenta * 50)) // 10
    cinco = (v_saque - (centena * 100) - (cinquenta * 50) - (dez * 10)) // 5
    um = v_saque - (centena * 100) - (cinquenta * 50) - (dez * 10) - (cinco * 5)

    print('\nConfira a quantidade de notas: ')
    if centena > 0:
        print('Notas de R$ 100: {}' .format(int(centena)))
    if cinquenta > 0:
        print('Notas de R$ 50: {}'.format(int(cinquenta)))
    if dez > 0:
        print('Notas de R$ 10: {}' .format(int(dez)))
    if cinco > 0:
        print('Notas de R$ 5: {}'.format(int(cinco)))
    if um > 0:
        print('Notas de R$ 1: {}'.format(int(um)))




