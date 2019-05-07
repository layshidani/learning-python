print('---' * 25)
print('Fatoriais')
print('---' * 25)

num = int(input('\nInforme um nº inteiro positivo para que possamos calcular o seu fatorial: '))

while num < 0:
    print('O número deve ser um inteiro positivo. Tente outra vez.')
    num = int(input('\nInforme um nº inteiro para que possamos calcular o seu fatorial: '))
else:
    fatorial = 1

    for n in range(1, num + 1):
        fatorial *= n

print('\n>>> O fatorial de {} é {:,}' .format(num, fatorial))
