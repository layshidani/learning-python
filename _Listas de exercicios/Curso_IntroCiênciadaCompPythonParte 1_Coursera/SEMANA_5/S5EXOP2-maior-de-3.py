# coding: utf-8

print('-=-' * 10)
print('Maior de 3')
print('-=-' * 10)

def maximo(x, y, z):
	'''Informa qual o maior número entre os três números informados'''
	lista = [x, y, z]
	return max(lista)


x = int(input('Insira um número: '))
y = int(input('Insira outro número: '))
z = int(input('Insira outro número: '))

maximo(x, y, z)
