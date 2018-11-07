# coding: utf-8

print('''Exercício Python 026: Faça um programa que leia uma frase pelo teclado e 
\n-mostre quantas vezes aparece a letra "A", 
\n-em que posição ela aparece a primeira vez e 
\n-em que posição ela aparece a última vez.''')

frase = str(input('Digite uma frase: ').upper())
print('Na frase digitada, a letra A aparece: {} vezes.'.format(frase.count('A')))
print('A primeira vez em que a letra A apareceu na frase, foi na posição {}'.format(frase.find('A')+1))
print('A última vez em que a letra A apareceu na frase, foi na posição {}'.format(frase.rfind('A')+1))
