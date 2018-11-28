# coding=utf-8

def primo(n):
    count = 2
    while count < n:
        if n % count == 0:
            return False
        else:
            count += 1
    return True


def maior_primo(n):
    while n > 2:
        if primo(n) == True:
            return n
        else:
            n -= 1
    return n

i = 1

while i < 2:
    i = int(input("Digite um nº inteiro >= 2: "))

print(maior_primo(i))
