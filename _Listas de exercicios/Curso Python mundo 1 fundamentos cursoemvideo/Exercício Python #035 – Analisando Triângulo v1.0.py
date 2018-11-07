print('''\nExercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao 
usuário se elas podem ou não formar um triângulo.\n''')

print('-=-' * 21)
reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda reta: '))
reta3 = float(input('Informe o valor da terceira reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('Os segmentos informados \033[1;34m>>> PODEM <<<\033[m formar um triângulo!')
else:
    print('Os segmentos informados \033[1;31m>>> NÃO PODEM <<<\033[m formar um triângulo!')

print('-=-' * 21)
