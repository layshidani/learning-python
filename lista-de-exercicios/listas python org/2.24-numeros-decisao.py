# coding: utf-8
# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.

print('\nOlá!\n\nVamos analisar números!!!')
oque = str(input('\nQue tipo de análise você deseja fazer? (1/2/3) '
                 '\nInsira:'
                 '\n1 - descobrir se é par ou ímpar'
                 '\n2 - descobrir se é positivo ou negativo'
                 '\n3 - descobrir se é inteiro ou decimal..'))

n1 = float(input('\nInsira um nº: '))
n2 = float(input('Insira mais um nº: '))

if oque == '1':
    print('\nVamos analisar se seus nº são par ou ímpar...')
    print ('...Concluímos a análise...')
    if n1 % 2 == 0:
        print('\nO nº {} é PAR!' .format(n1))
    else:
        print('\nO nº {} é IMPAR!' .format(n1))
    if n2 % 2 == 0:
        print('\nO nº {} é PAR!'.format(n2))
    else:
        print('\nO nº {} é IMPAR!'.format(n2))

elif oque == '2':
    print('\nVamos analisar se seus nº são positivos ou negativos...')
    print ('...Concluímos a análise...')
    if n1 < 0:
        print('\nO nº {} é NEGATIVO.' .format(n1))
    else:
        print('\nO nº {} é POSITIVO.'.format(n1))
    if n2 < 0:
        print('\nO nº {} é NEGATIVO.' .format(n2))
    else:
        print('\nO nº {} é POSITIVO.'.format(n2))

elif oque == '3':
    print('\nVamos analisar se seus nº são inteiros ou decimais...')
    print ('...Concluímos a análise...')
    if n1 == int(n1):
        print('\nO nº {} é INTEIRO.'.format(n1))
    else:
        print('\nO nº {} é DECIMAL.'.format(n1))
    if n2 == int(n2):
        print('\nO nº {} é INTEIRO.'.format(n2))
    else:
        print('\nO nº {} é DECIMAL.'.format(n2))

else:
    print('\nNão entendi o comando...Tente de novo.')
