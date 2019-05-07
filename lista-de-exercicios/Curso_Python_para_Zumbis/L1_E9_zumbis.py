#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado
d = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Qual a quantidade de km percorridos? '))
p = (60*d)+ (0.15*km)
print('\nO valor total a ser pago é R$: ', p)

print('\n***Fim***')

