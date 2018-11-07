# coding: utf-8

salario_antes = float(input('Informe o salário do funcionário R$ '))
aumento_perc = float(input('Informe o % de aumento salarial '))
aumento = salario_antes * (aumento_perc/100)
salario_agora = salario_antes + aumento

print('\nParabéns você teve um acréscimo de R$ {:.2f}!'.format(aumento))
print('O salário agora é R$ {:.2f}'.format(salario_agora))
