# coding: utf-8

print('-' * 40)
print('Somador de número inteiro'.center(40, '-'))
print('-' * 40)

n = int(input('\nDigite um número inteiro: '))

i = 0

if n == 0 or n == 1:
	print('não primo')
else:
	for divisor in range(2, n):
		if (n % divisor) == 0 and (n != divisor):
			i += 1

	if i != 0:
		print('não primo')
	else:
		print('primo')
