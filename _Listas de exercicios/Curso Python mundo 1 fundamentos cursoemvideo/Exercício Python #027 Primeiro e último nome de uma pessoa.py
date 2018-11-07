# coding: utf-8

from typing import List

print('''Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, 
\nmostrando em seguida o primeiro e o último nome separadamente.''')
a = str(input("Digite seu nome completo: ").title).strip()

nome = a.split()
print('\nSeu primeiro nome é: {}'.format(nome[0]))

print('\nSeu ultimo nome é: {}'.format(nome[-1]))

print('Muito prazer em te conhecer!')
