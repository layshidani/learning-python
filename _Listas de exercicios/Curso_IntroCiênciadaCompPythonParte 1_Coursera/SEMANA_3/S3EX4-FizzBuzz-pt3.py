# coding: UTF-8

print('---' * 15)
print('FizzBuzz - Parte 3 (Divisível por 3 e por 5')
print('---' * 15)

num = int(input('Insira um número inteiro: '))

if num % 3 == 0 and num % 5 == 0:
    print('\nFizzBuzz')
else:
    print(num)