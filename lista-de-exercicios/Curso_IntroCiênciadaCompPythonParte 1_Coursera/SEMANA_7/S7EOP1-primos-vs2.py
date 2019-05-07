# coding=utf-8


def primos(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True


def n_primos(num):
    aux = 1
    i = 0
    while aux < num:
        aux += 1
        if primos(aux):
            i += 1
    return i


num = int(input("Digite um número > 2: "))

print(n_primos(num))

