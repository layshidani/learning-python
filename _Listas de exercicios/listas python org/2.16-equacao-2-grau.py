print('''\n16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;\n''')

print('-=-' * 21)
print('\033[1;30;44mVamos encontrar as raízes de uma equação de 2º grau.\033[m')
a = int(input('\nInforme o valor de (a): '))
if a == 0:
    print('\n\033[31mA equação não é de 2º grau. \n >>>Programa Encerrado!<<<\033[m')
else:
    b = int(input('\nInforme o valor de (b): '))
    c = int(input('\nInforme o valor de (c): '))

    delta = (b ** 2) - (4 * a * c)

    raiz_delta = delta ** (1/2)
    x1 = (- b + raiz_delta) / (2 * a)
    x2 = (- b - raiz_delta) / (2 * a)

    if delta < 0:
        print('\n\033[31mEsta equação não possui raizes reais. \n>>>Programa Encerrado...<<<\033[m')
    elif delta == 0:
        print('\nEsta equação possui \033[34m1 raiz real: ({:.2f}, {:.2f})\033[m' .format(x1, x2))
    elif delta > 0:
        print('\nEsta equação possui \033[34m2 raizes reais: ({:.2f}, {:.2f})\033[m' .format(x1, x2))

print('-=-' * 21)
