print('''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o aumento de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.''')

print('**********************************************************************************')
salario = float(input('\n >>> >>> >>> Informe seu salário atual R$ '))

if salario <= 280:
    percentual = 20
    aumento = (percentual / 100) * salario
    salario_novo = salario + aumento
elif 280 < salario <= 700:
    percentual = 15
    aumento = (percentual / 100) * salario
    salario_novo = salario + aumento
elif 700 < salario < 1500:
    percentual = 10
    aumento = (percentual / 100) * salario
    salario_novo = salario + aumento
elif salario >= 1500:
    percentual = 5
    aumento = (percentual / 100) * salario
    salario_novo = salario + aumento

print('''\nSalário antes do reajuste: R$ {:.2f} 
            Percentual de ajuste {:.2f}%
            Aumento R$ {:.2f}
            \n>>> >>> >>> Salário após reajuste: R$ {:.2f}''' .format(salario, percentual, aumento, salario_novo))


