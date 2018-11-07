print('Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit')

print('\n===Vamos converter Celsius para Farenheit===')
C = float(input('Informe a temperatura em Celsius: '))
F = (C * (9 / 5)) + 32
print('{:.2f} C = {:.2f} F' .format(C, F))