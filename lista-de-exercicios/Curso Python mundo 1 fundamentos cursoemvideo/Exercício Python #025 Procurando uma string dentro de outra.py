# coding: utf-8

print('Exercício Python 025: Crie um programa que leia o nome de uma pessoa \ne diga se ela tem "SILVA" no nome.')
nome = str(input('Digite o nome completo: ').upper())
print('Há SILVA no nome digitado? : {}'.format('SILVA ' in nome))
