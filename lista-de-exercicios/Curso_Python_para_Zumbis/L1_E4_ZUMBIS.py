print('L1_E4_Zumbis \n====Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.====')
s1 = float(input('Digite o valor do salário: R$'))
aumento = int(input('Insira a porcentagem de aumento que recebeu: %'))
s2 = s1 * (1 + aumento/100)
print('\nSeu novo salário é R$ ', s2)
print('O aumento do seu salário foi de R$ ', s2-s1)
print('\nParabéns pelo aumento salarial!')

print('\n***FIM***')