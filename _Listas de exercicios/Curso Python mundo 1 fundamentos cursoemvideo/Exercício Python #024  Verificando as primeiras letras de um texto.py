# coding: utf-8

print('Exercício Python 024: Crie um programa que leia o nome de uma cidade e \ndiga se ela começa ou não com o nome "SANTO".')
nome = str(input('Digite o nome da cidade: ').upper()).strip()
if nome[:5] == 'SANTO ':
    print('Correto')
else:
    print('Errado!')
