# coding: utf-8
import math

print('-=-' * 15)
print('Calculadora Raiz Quadrada')
print('-=-' * 15)

print('Modelo: ax² + bx + c = 0 \n\n--> Seguindo o modelo, Informe: ')

a = float(input('\nValor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

delta = b**2 - (4*a*c)

if delta < 0:
	print('esta equação não possui raízes reais')
else:
    raiz1 = (-b + math.sqrt(delta)) / 2*a
    raiz2 = (-b - math.sqrt(delta)) / 2*a
    if raiz1 == raiz2:
        print('a raiz desta equação é', raiz1)
    elif raiz1 == 0 and raiz2 != 0:
        print('a raiz desta equação é', raiz2)
    elif raiz1 != 0 and raiz2 ==0:
        print('a raiz desta equação é', raiz1)
    elif raiz1 != 0 and raiz2 != 0:
        if raiz1 > raiz2:
            print('as raízes da equação são', raiz2, 'e', raiz1)
        else:
            print('as raízes da equação são', raiz1, 'e', raiz2)