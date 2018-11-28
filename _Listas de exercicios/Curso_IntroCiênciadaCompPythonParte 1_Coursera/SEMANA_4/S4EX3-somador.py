# coding: utf-8

print('-' * 40)
p = 'Somador de dígitos'
print(p.center(40, '-'))
print('-' * 40)

n = str(input('\nInsira um número inteiro: '))


lista = []
soma = 0

for digito in n:
    lista.append(int(digito))

print(sum(lista))