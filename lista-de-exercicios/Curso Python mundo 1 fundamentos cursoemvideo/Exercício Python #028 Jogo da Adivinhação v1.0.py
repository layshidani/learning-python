print('''\nExercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.''')

import random

numero = random.randint(0, 5)

print('-=-' * 21)
n = int(input('\nEu escolhi um nº entre 0 e 5. Tente adivinhar qual foi: '))
print('-=-' * 21)
if (n == numero):
    print('Aee, você acertou! Eu escolhi o nº: {}'.format(numero))
else:
    print('Você errou :/. Eu tinha escolhido o nº {}'.format(numero))
