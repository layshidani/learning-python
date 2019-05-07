print('-=-' * 15)
print('Distância entre dois pontos')
print('-=-' * 15)

num1 = int(input('\nInsira um número: '))
num2 = int(input('\nInsira um número: '))
num3 = int(input('\nInsira um número: '))
num4 = int(input('\nInsira um número: '))

x_ponto_1 = num1
y_ponto_1 = num2

x_ponto_2 = num3
y_ponto_2 = num4

distancia = ((x_ponto_2 - x_ponto_1) ** 2 + (y_ponto_2 - y_ponto_1) ** 2) ** (1/2)

print(distancia)

if distancia >= 10:
	print('\nlonge')
else:
	print('\nperto')