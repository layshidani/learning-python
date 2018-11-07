print('''Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.''')


km = float(input('\nInforme a distância da viagem em km: '))

if (km <= 200):
    preco = km * 0.50
else:
    preco = km * 0.45

print('O preço para essa viagem de {:.2f} km é \033[46mR$ {:.2f}\033[m' .format(km, preco))
print('\033[34mBoa viagem!\033[m')
