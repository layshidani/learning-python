
# coding: utf-8

#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
#cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
print('===Vamos calcular o seno, cosceno e tangente a partir de um ângulo informado===')
angulo = float(input('\nDigite o Angulo: '))

seno = sin(radians(angulo))
print('O seno de {:.2f}° é {:.2f}'.format(angulo, seno))
coss = cos(radians(angulo))
print('O cosseno de {:.2f}° é {:.2f}'.format(angulo, coss))
tang = tan(radians(angulo))
print('A tangente de {:.2f}° é {:.2f}'.format(angulo, tang))

