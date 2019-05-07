# coding: UTF-8

# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

print('-=-' * 21)
print('Vamos calcular o seu aumento salárial!!!')
salario = float(input('Informe o valor de seu salário: R$ '))

if salario > 1250:
    aumento = 1250 * 0.1
    novo_salario = salario + aumento
    print('\nAumento (10%) R$ {:.2f}' .format(aumento))
    print('Salário após aumento R$ {:.2f}' .format(novo_salario))
else:
    aumento = 1250 * 0.15
    novo_salario = salario + aumento
    print('\nAumento (15%) R$ {:.2f}'.format(aumento))
    print('Salário após aumento R$ {:.2f}'.format(novo_salario))

print('-=-' * 21)
