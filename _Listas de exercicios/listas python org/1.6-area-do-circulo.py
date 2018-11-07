print('6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.')

from math import pi

print('Vamos calcular a área de um círculo')
r = float(input('Informe o valor do raio do círculo: '))
a = pi * (r ** 2)
print('A área é {:.2f}' .format(a))