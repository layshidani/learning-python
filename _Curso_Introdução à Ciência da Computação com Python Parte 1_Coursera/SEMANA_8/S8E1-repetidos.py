# coding=utf-8

def remove_repetidos(lista):
    lista = list(set(lista))
    return sorted(lista)


entrada = input("Informe uma lista de números: ")

lista = [int(x) for x in entrada.split()]

print(remove_repetidos(lista))