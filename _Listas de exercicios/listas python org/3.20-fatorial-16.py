print('---' * 25)
print('Fatoriais')
print('---' * 25)

num = int(input('\nInforme um nº inteiro para que possamos calcular o seu fatorial \nDeve estar entre 1 e 16: '))

while True:
    while num < 0 or num > 16:
        print('O número deve ser um inteiro positivo. Tente outra vez.')
        num = int(input('\nInforme um nº inteiro para que possamos calcular o seu fatorial: '))
    else:
        fatorial = 1

        for n in range(1, num + 1):
            fatorial *= n

    print('\n>>> O fatorial de {} é {:,}' .format(num, fatorial))

    continuar = str(input('\nDeseja calcular outro nº? (s/n)').lower())
    if continuar == 'n':
        print('\n\n>>>Finalizando o programa...<<<')
        break
    else:
        num = int(
            input('\nInforme um nº inteiro para que possamos calcular o seu fatorial \nDeve estar entre 1 e 16: '))