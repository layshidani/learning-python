# coding: utf-8

#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade 
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Informe a quantidade de dias pelos quais o veículo foi alugado: '))
km = float(input('Informe a quantidade de km percorridos pelo veículo: '))
preco = (dias * 60) + (km * 0.15)
print('\nO valor a ser pago é de R$ {:.2f}'.format(preco))

