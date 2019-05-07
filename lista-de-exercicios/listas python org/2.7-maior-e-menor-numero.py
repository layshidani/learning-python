print('Faça um Programa que leia três números e mostre o maior e o menor deles.')

n1 = float(input('Insira um nº: '))
n2 = float(input('Insira outro nº: '))
n3 = float(input('Insira outro nº: '))

if n1 < n2 < n3:
    print('O maior nº é {} e o menor é {}' .format(n3, n1))
elif n3 < n2 < n1:
    print('O maior nº é {} e o menor é {}'.format(n1, n3))
elif n2 < n1 < n3:
    print('O maior nº é {} e o menor é {}'.format(n3, n2))
elif n2 < n3 < n1:
    print('O maior nº é {} e o menor é {}'.format(n1, n2))
elif n3 < n1 < n2:
    print('O maior nº é {} e o menor é {}'.format(n2, n3))
elif n1 < n3 < n2:
    print('O maior nº é {} e o menor é {}'.format(n2, n1))


#ou.. usando listas:
#lista = []
#n1 = lista.append(float(input('Insira um nº: ')))
#n2 = lista.append(float(input('Insira outro nº: ')))
#n3 = lista.append(float(input('Insira outro nº: ')))

#print('\nO maior número é ', max(lista))
#print('O menor número é ', min(lista))