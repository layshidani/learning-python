# coding: UTF-8

print('---' * 20)
print('Dígito de dezenas de um número inteiro')
print('---' * 20)

numero = int(input('Digite um número inteiro: '))

milhar = numero // 1000
centena = (numero - (milhar * 1000)) // 100
dezena = (numero - (milhar * 1000) - (centena * 100)) // 10
unidade = (numero - (milhar * 1000) - (centena * 100) - (dezena * 10))

print('\nO dígito das dezenas é', dezena)
