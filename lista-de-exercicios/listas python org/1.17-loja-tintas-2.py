print('''17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
\nInforme ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
>>>comprar apenas latas de 18 litros;
>>>comprar apenas galões de 3,6 litros;
>>>misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os
valores para cima, isto é, considere latas cheias.''')

from math import ceil

area = float(input('\nInforme o tamanho da área a ser pintada: '))
litros = ceil((area / 6) * 1.1)

#latas de 18 litros
latas_18 = ceil(litros / 18)
preco_latas = latas_18 * 80.00

#galões de 3,6 litros
galao_3_6 = ceil(litros / 3.6)
preco_galao = galao_3_6 * 25.00

#misturado
mix_latas = int(litros / 18)
mix_galoes = ceil((litros - (litros / 18)) / 3.6)
preco_mix = (mix_latas * 80 + mix_galoes * 25)




print('\n\nVocê deverá comprar {:.2f} litros de tinta.\n' .format(litros))
print('1ª opção: {:.2f} lata(s) de 18 litros\nCusto: R$ {:.2f}' .format(latas_18, preco_latas))
print('\n2ª opção: {:.2f} galões de 3,6 litros\nCusto: R$ {:.2f}' .format(galao_3_6, preco_galao))
print('\n3ª opção: MISTA >>> {:.2f} latas de 18 litros + {:.2f} galões de 3.6 litros'
      '\nCusto: R$ {:.2f}' .format(mix_latas, mix_galoes, preco_mix))

#O Mais barato
print('\n\nAnalisando as 3 possibilidades...\nO melhor custo para você é: ')
if preco_mix < preco_galao and preco_mix < preco_latas:
    print('Compre latas e galões: R$ {:.2f} >>> 3ª opção' . format(preco_mix))
elif preco_latas < preco_mix and preco_latas < preco_galao:
    print('Compre somente latas: R$ {:.2f} >>> 1ª opção' .format(preco_latas))
elif preco_galao < preco_latas and preco_galao < preco_mix:
    print('Compre somente galões: R$ {:.2f} >>> 2ª opção' .format(preco_galao))

