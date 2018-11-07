print('----' * 30)
print('Verificador de número primo')
print('----' * 30)

divisores = 0
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

        if divisores > 0:
            print('O nº {} NÃO é primo...' .format(numero))
        else:
            print('O nº {} é primo!' .format(numero))
