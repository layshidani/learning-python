print('\nExercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')

print('-=-' * 21)
lista = []
n1 = lista.append(int(input('\nInforme um nº: ')))
n2 = lista.append(int(input('Informe outro nº: ')))
n3 = lista.append(int(input('Informe outro nº: ')))

print('\n>>> Números informados: ', lista, '<<<')
print('Menor nº: {}' .format(min(lista)))
print('MAIOR nº: {}' .format(max(lista)))

print('-=-' * 21)
