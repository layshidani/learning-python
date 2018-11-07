# coding: utf-8
# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

print('\nVamos analisar se um nº é par ou impar...')
n = int(input('\nInsira um nº inteiro qualquer: '))

if n % 2 == 0:
    print('O nº {} é par.' .format(n))
else:
    print('O nº {} é impar.' .format(n))
