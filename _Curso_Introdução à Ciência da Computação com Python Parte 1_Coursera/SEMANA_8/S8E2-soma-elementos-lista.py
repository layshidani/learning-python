# coding=utf-8


def soma_elementos(lista):
    soma = sum(lista)
    return soma


entrada = input("Insira uma lista de números inteiros: ")

lista = [int(x) for x in entrada.split()]

print(soma_elementos(lista))