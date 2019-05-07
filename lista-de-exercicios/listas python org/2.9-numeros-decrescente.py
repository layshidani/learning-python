print('Faça um Programa que leia três números e mostre-os em ordem decrescente')

n1 = int(input('\n>>> Informe um nº inteiro: '))
n2 = int(input('\n>>> Informe outro nº inteiro: '))
n3 = int(input('\n>>> Informe outro nº inteiro: '))

if n1 > n2 > n3:
    print('Ordem decrescente: {}, {}, {}' .format(n1, n2, n3))
elif n1 > n3 > n2:
    print('Ordem decrescente: {}, {}, {}'.format(n1, n3, n2))
elif n2 > n1 > n3:
    print('Ordem decrescente: {}, {}, {}'.format(n2, n1, n3))
elif n2 > n3 > n1:
    print('Ordem decrescente: {}, {}, {}'.format(n2, n3, n1))
elif n3 > n1 > n2:
    print('Ordem decrescente: {}, {}, {}'.format(n3, n1, n2))
elif n3 > n2 > n1:
    print('Ordem decrescente: {}, {}, {}'.format(n3, n2, n1))