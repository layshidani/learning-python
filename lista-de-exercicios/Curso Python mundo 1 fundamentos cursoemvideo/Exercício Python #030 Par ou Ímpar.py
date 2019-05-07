print('\nExercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.')

print('\033[1;96m-=-\033[m' * 21)
n = int(input('Insira um nº: '))

if (n % 2 == 0):
    print('\nO nº {} é \033[;7mPAR\033[m' .format(n))
else:
    print('\nO nº {} é \033[;7mIMPAR\033[m' .format(n))

print('\033[1;96m-=-\033[m' * 21)
