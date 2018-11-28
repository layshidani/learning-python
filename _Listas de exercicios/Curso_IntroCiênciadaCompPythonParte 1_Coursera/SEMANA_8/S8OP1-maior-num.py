# coding=utf-8

def maior_elemento(lista):
    maior = max(lista)
    return maior


x = input("Informe uma lista de números: ")
lista = [int(x) for x in x.split()]
print(maior_elemento(lista))