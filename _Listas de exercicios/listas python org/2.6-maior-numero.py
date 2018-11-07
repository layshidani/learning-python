print('Faça um Programa que leia três números e mostre o maior deles')

n1 = float(input('Insira um nº: '))
n2 = float(input('Insira outro nº: '))
n3 = float(input('Insira outro nº: '))

if n1 > n2 and n1 > n3:
    print('O maior número é {}' .format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior número é {}' .format(n2))
elif n3 > n1 and n3 > n2:
    print('O maior número é {}' .format(n3))



#ou.. usando listas:
#lista = []
#n1 = lista.append(float(input('Insira um nº: ')))
#n2 = lista.append(float(input('Insira outro nº: ')))
#n3 = lista.append(float(input('Insira outro nº: ')))

#print('O maior número é ', max(lista))