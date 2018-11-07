# coding: UTF-8

print('---' * 15)
print('Verificando ordenação')
print('---' * 15)

num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira outro número inteiro: '))
num3 = int(input('Insira outro número inteiro: '))


if num1 < num2 < num3:
    print('crescente')
else:
    print('não está em ordem crescente')