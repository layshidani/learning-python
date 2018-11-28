print('-=-' * 10)
print('Maior número')
print('-=-' * 10)

def maximo(n1, n2):
	lista = [n1, n2]
	print('\nEntre os números: ', lista, 'O maior é:')
	return max(lista)

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

maximo(n1, n2)



