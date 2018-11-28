# coding=utf-8

def eh_hipotenusa(n):
    i = 1
    while i <= n:
        u = 1
        while u <= n:
            hipotenusa = (i ** 2 + u ** 2) ** (0.5)
            if hipotenusa == n:
                return True
            u += 1
        i += 1

    return False


def soma_hipotenusas(n):
    aux = 1
    soma = 0
    while aux <= n:
        if eh_hipotenusa(aux):
            soma += aux
        aux += 1
    return soma


n = int(input("Olá! Digite um número: "))

print(soma_hipotenusas(n))