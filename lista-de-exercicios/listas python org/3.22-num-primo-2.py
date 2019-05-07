# coding: UTF-8
print('----' * 30)
print('Verificador de número primo')
print('----' * 30)

divisores = 0
lista = []

numero = int(input('\nInforme um nº inteiro positivo para verificar se ele é primo: '))

while numero < 0:
    numero = int(input('\nInforme um nº inteiro positivo para verificar se ele é primo: '))
else:
    if numero == 0 or numero == 1:
        print('O nº {} NÃO é primo...'.format(numero))
    else:
        x = range(2, numero)
        for i in x:
            if (numero % i) == 0 and (i != numero):
                divisores += 1
                lista.append(i)

        lista_2 = [1, numero]
        lista_2 += lista
        lista_2.sort()

        if divisores > 0:
            print('\nO nº {} NÃO é primo' .format(numero))
            print('{} é divisível por: {}' .format(numero, lista_2))
        else:
            print('\nO nº {} é primo!' .format(numero))
