print('Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser '
      'pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de'
      '18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.')

area = float(input('\nInforme a medida em m² do local a ser pintado: '))
litros = (area / 3)

latas = int(litros / 18)

if (litros % 18 != 0):
    latas += 1

preco = latas * 80.00

print('\n\nPara pintar {:.2f} m²'
      '\nSerão necessárias {:.2f} latas de tinta'
      '\n\nCom cada lata de 18 litros custando R$ 80,00,'
      '\nPreço total R$ {:.2f}' .format(area, latas, preco))
