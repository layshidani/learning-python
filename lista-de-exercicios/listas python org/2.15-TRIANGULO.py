print('''\nFaça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;''')

print('-=-' * 21)
reta1 = float(input('\nInforme o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda reta: '))
reta3 = float(input('Informe o valor da terceira reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('\nOs segmentos informados \033[1;34m>>> PODEM <<<\033[m formar um triângulo!')
    if (reta1 == reta2 == reta3):
        print('\nÉ um triângulo EQUILÁTERO!')
    elif (reta1 == reta2) or (reta1 == reta3) or (reta2 == reta3):
        print('\nÉ um triângulo ISÓSCELES!')
    elif (reta1 != reta2 != reta3):
        print('\nÉ um triângulo ESCALENO!')
else:
    print('Os segmentos informados \033[1;31m>>> NÃO PODEM <<<\033[m formar um triângulo!')

print('-=-' * 21)
