ano = int(input('Digite o ano que você deseja saber se é bissexto: '))
por_4 = ano % 4
por_400 = ano % 400
por_100 = ano % 100
if por_4 == 0 and por_400 and por_100:
    print(':) Sim! {} é um ano BISSEXTO!'.format(ano))
else:
    print(':/ {} não é um ano bissexto...'.format(ano))