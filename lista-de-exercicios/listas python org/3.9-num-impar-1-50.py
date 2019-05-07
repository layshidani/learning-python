print('\n>>> Nº impar de 1 a 50 <<<')
seq = range(1, 51)
list(seq)

impar = []

for num in seq:
    teste = num % 2
    while teste != 0 and num not in impar:
        impar.append(num)

print(impar)
print('Quantidade de nº impar: {}' .format(len(impar)))
