# coding: utf-8

print('-=-' * 20)
print('Maior Primo')
print('-=-' * 20)

def maior_primo(n):
	'''Informa o maior nº primo <= ao nº informado como parâmetro'''
	primos = []
	for numero in range(n):
		contador = 0
		for divisor in range(n):
			if numero % (divisor + 1) == 0 and numero != divisor:
				contador += 1
		if contador == 2:
			primos.append(numero)

	return max(primos)


n = int(input('Informe um número natural >= a 2: '))

while True:
	if n < 2:
		print('\nValor informado incorreto. O valor deve ser maior ou igual a 2.')
		n = int(input('Informe um número natural >= a 2: '))
	else:
		maior_primo(n)
		break
