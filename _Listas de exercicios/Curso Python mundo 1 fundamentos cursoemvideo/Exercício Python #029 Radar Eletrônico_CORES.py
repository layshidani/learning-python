print('''\nExercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.''')

velocidade = float(input('\nQual é a velocidade atual do carro? (km/h): '))

multa = (velocidade - 80) * 7.0

print('-=-' * 21)
if velocidade <= 80:
    print('\n\033[1;30;42mMotorista dentro do limite de velocidade\033[m \033[0;32m :) '
          '\n>>>>> Nenhuma multa a ser aplicada! <<<<< \033[m')

else:
    print('\n\033[4;31mLimite de velocidade excedido!!!\033[m')
    print('\033[1;30;41m >>>> MULTADO! <<<<<\033[m \033[1;31mValor da multa: R$ {:.2f}\033[m \n' .format(multa))

print('-=-' * 21)
