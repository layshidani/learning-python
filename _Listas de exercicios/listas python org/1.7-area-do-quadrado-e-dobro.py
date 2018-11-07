print('7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.')

print('\nVamos calcular a área de um quadrado')
x = float(input('Informe o valor do lado x: '))
y = float(input('Informe o valor do lado y: '))
a = x * y
a2 = a * 2

print('\n>>> A área é {:.2f}' .format(a))
print('>>> O dobro da área é {:.2f}' .format(a2))