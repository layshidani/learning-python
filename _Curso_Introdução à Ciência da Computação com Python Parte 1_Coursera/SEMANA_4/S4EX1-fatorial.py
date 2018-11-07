# coding: utf-8

print('-=-' * 15)
print('Fatorial')
print('-=-' * 15)

n = int(input('\nInsira um número natural para calcularmos seu Fatorial: '))

contador = 1
n_fatorial = 1

while contador <= n:
	n_fatorial *= contador
	contador += 1
		
print(n_fatorial)
