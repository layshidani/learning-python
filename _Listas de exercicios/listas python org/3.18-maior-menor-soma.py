print('\nIremos verificar um conjunto de números e definir o maior valor, o menor valor e a soma de todos.')

qtd = int(input('\nInforme a quantidade de números que deverão ser analisados: '))
while qtd < 3:
    print('Erro. Quantidade deve ser de no mínimo 3 números, tente de novo...')
    qtd = int(input('\nInforme a quantidade de números que deverão ser analisados: '))
else:
    numeros = []
    print('Você deve inserir {} números para formar o conjunto..' .format(qtd))
    numeros.append(int(input('Informe um nº: ')))

    while len(numeros) < qtd:
        numeros.append(int(input('Informe um nº: ')))
    else:
        print('Ok. Vamos analisar!')

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

print('Análise completa!')
print('\nO MAIOR número do conjunto {} é --> {}' .format(numeros, max(numeros)))
print('O MENOR número do conjunto {} é --> {}' .format(numeros, min(numeros)))
print('A soma dos números é {}' .format(sum(numeros)))

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

