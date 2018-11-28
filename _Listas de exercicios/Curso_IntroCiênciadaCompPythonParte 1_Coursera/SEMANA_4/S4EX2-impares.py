# coding: utf-8

print('-=-' * 15)
print('n primeiros números ímpares')
print('-=-' * 15)

n = int(input('\nInsira um número natural: '))

contador = 0
impar = 1

print(impar)

while contador < n-1:
	impar += 2
	contador += 1
	print(impar)

