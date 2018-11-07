print('12. Tendo como dados de entrada a altura de uma pessoa, '
      'construa um algoritmo que calcule seu peso ideal, usando a'
      'seguinte fórmula: (72.7 * altura) - 58)')

print('\n===Vamos calcular seu peso ideal!===')
altura = float(input('\nInforme a sua altura (m): '))
peso_ideal = (72.7 * altura) - 58
print('\nAnalisamos seus dados...\n...Fizemos varias contas mágicas...'
      '\n...e descobrimos que seu peso ideal é {:.2f} kg' .format(peso_ideal))
