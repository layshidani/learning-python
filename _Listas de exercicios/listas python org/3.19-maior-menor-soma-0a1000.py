print('\nIremos verificar um conjunto de números e definir o maior valor, o menor valor e a soma de todos.')

numeros = []

qtd = int(input('\nInforme a quantidade de números que deverão ser analisados: '))

while qtd < 3:
    print('Erro. Quantidade deve ser de no mínimo 3 números, tente de novo...')
    qtd = int(input('\nInforme a quantidade de números que deverão ser analisados: '))
else:
    print('\nVocê deve inserir {} números para formar o conjunto..\nUse apenas números de 0 a 1000.' .format(qtd))

    while len(numeros) < qtd:
        numero = int(input('\nInforme um nº: '))

        if 0 < numero < 1000:
            numeros.append(numero)
            print('>>>Este Número foi adicionado ao conjunto com sucesso<<<')
        else:
            print('\nOs números devem ser entre 0 e 1000. Tente de novo.')
            pass

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

print('Análise completa!')
print('\nO MAIOR número do conjunto {} é --> {}' .format(numeros, max(numeros)))
print('O MENOR número do conjunto {} é --> {}' .format(numeros, min(numeros)))
print('A soma dos números é {}' .format(sum(numeros)))
print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
