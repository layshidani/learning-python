# coding=utf-8

lista = []
num = -1
while num != 0:
    num = int(input("Digite um número: "))
    if num != 0:
        lista.append(num)

lista2 = []
for elemento in reversed(lista):
    print(elemento)
