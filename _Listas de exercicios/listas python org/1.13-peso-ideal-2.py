print('13. Tendo como dado de entrada a altura (h) de uma pessoa,'
      'construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:'
      '\na. Para homens: (72.7*h) - 58'
      '\nb. Para mulheres: (62.1*h) - 44.7')

print('\nOlá! Vamos calcular seu peso ideal!')
h = float(input('\nInforme qual a sua altura (m): '))
sx = str(input('Você é do sexo feminino ou masculino? \nInsira: \nf para feminino ou \nm para masculino: '))
if (sx == 'f'):
    peso_ideal = (62.1 * h) - 44.7
    print('Seu peso ideal é: {:.2f} Kg'.format(peso_ideal))
elif (sx == 'm'):
    peso_ideal = (72.7 * h) - 58
    print('Seu peso ideal é: {:.2f} Kg' .format(peso_ideal))
else:
    print('Tente de novo...')
