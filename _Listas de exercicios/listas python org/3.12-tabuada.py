print('\n\n>>>TABUADA<<<')

m = int(input('\nInforme: A tabuada de qual nº você deseja saber? '))

print('Resultado da Tabuada de {}:' .format(m))

for num in range(1, 11):
    print(m, ' x ', num, ' = ', (m * num))