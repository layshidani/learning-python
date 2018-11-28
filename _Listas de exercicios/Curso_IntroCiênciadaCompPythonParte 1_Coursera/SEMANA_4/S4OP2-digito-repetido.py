print('-=-' * 15)
print('Digito adjacente igual'.center(15, '-'))
print('-=-' * 15)

n = int(input('Insira um número inteiro: '))

print('\nO número', n, 'possui dígitos adjacentes iguais?')	

n_anterior = n % 10
n = n // 10
igual = False
i = 0

while n > 0 and not igual:
    n_atual = n % 10
    if n_atual == n_anterior:
        igual = True
    else:
        i += 1
    n_anterior = n_atual
    n = n // 10
        
if igual:
	print('sim')
else:
	print('não')
