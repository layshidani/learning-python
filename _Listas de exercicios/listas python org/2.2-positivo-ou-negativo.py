print('Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo')

number = int(input('\nInsira um número qualquer e eu vou lhe dizer se ele é positivo ou negativo: '))

if number < 0:
    print(number, 'é negativo. \nAcertei?')

elif number > 0:
    print(number, 'é positivo. \nAcertei?')

elif number == '0':
    print('\nO nº digitado é zero!')