# coding: utf-8
# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

print('\nVamos analisar se um nº é inteiro ou decimal...')

n = float(input('\nInforme um nº para analisarmos: '))

if n == int(n):
    print('O nº {:.0f} é um inteiro!' .format(n))
else:
    print('O nº {} é um decimal...' .format(n))