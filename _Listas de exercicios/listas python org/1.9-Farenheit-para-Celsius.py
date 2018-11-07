print('Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius')
#C = (5 * (F-32) / 9)

print('\n===Vamos converter Farenheit para Celsius!===')
F = float(input('Informe a temperatura em Farenheit: '))
C = (5 * (F - 32) / 9)
print('\n{:.2f} F = {:.2f} C' .format(F, C))