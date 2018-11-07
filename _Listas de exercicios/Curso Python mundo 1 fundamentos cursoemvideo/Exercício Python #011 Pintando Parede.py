# coding: utf-8

print('Vamos calcular a quantidade de tinta necessária para pintar a parede!')
#1 litro de tinta para cada 2 m^2 de parede
l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l * h 
t = (a/2)
print('\nA sua parede tem a dimensão {:.2f} x {:.2f} m, e sua área é de {:.2f} m²'.format(l, h, a))
print('Para pintar essa parede, será necessário {:.2f} l de tinta'.format(t))

