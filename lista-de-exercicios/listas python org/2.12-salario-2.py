print('''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
***Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00***''')

print('\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.')
valor_hora = float(input('Informe quanto você recebe por hora trabalhada: R$ '))
horas_trabalhadas = float(input('Informe quantas horas vocÊ trabalhou neste mês: '))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    desconto_ir = salario_bruto * 0.00
    desconto_inss = salario_bruto * 0.10
    desconto_fgts = salario_bruto * 0.11
    desconto_sindicato = salario_bruto * 0.03
    total_de_descontos = desconto_ir + desconto_inss + desconto_sindicato
    salario_liquido = salario_bruto - total_de_descontos
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print('''\n
        Salário bruto ({} * {}): R$ {:.2f}' 
        (-) IR (0% ISENTO): R$ {:.2f}
        (-) INSS (10%): R$ {:.2f}
         FGTS (11% não descontado do salário): R$ {:.2f}
         Total de descontos: R$ {:.2f}
         Salário líquido: R$ {:.2f}
         '''.format(valor_hora, horas_trabalhadas, salario_bruto, desconto_ir, desconto_inss, desconto_fgts,
                    total_de_descontos, salario_liquido))
    print('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

elif 900 < salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
    desconto_inss = salario_bruto * 0.10
    desconto_fgts = salario_bruto * 0.11
    desconto_sindicato = salario_bruto * 0.03
    total_de_descontos = desconto_ir + desconto_inss + desconto_sindicato
    salario_liquido = salario_bruto - total_de_descontos
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print('''\n
    Salário bruto ({} * {}): R$ {:.2f}' 
    (-) IR (5%): R$ {:.2f}
    (-) INSS (10%): R$ {:.2f}
     FGTS (11% não descontado do salário): R$ {:.2f}
     Total de descontos: R$ {:.2f}
     Salário líquido: R$ {:.2f}
     '''.format(valor_hora, horas_trabalhadas, salario_bruto, desconto_ir, desconto_inss, desconto_fgts, total_de_descontos, salario_liquido))
    print('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
elif 1500 < salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
    desconto_inss = salario_bruto * 0.10
    desconto_fgts = salario_bruto * 0.11
    desconto_sindicato = salario_bruto * 0.03
    total_de_descontos = desconto_ir + desconto_inss + desconto_sindicato
    salario_liquido = salario_bruto - total_de_descontos
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print('''\n
        Salário bruto ({} * {}): R$ {:.2f}' 
        (-) IR (10%): R$ {:.2f}
        (-) INSS (10%): R$ {:.2f}
         FGTS (11% não descontado do salário): R$ {:.2f}
         Total de descontos: R$ {:.2f}
         Salário líquido: R$ {:.2f}
         '''.format(valor_hora, horas_trabalhadas, salario_bruto, desconto_ir, desconto_inss, desconto_fgts,
                    total_de_descontos, salario_liquido))
    print('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
elif salario_bruto > 2500:
    desconto_ir = salario_bruto * 0.20
    desconto_inss = salario_bruto * 0.10
    desconto_fgts = salario_bruto * 0.11
    desconto_sindicato = salario_bruto * 0.03
    total_de_descontos = desconto_ir + desconto_inss + desconto_sindicato
    salario_liquido = salario_bruto - total_de_descontos
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print('''\n
        Salário bruto ({} * {}): R$ {:.2f}' 
        (-) IR (20%): R$ {:.2f}
        (-) INSS (10%): R$ {:.2f}
         FGTS (11% não descontado do salário): R$ {:.2f}
         Total de descontos: R$ {:.2f}
         Salário líquido: R$ {:.2f}
         '''.format(valor_hora, horas_trabalhadas, salario_bruto, desconto_ir, desconto_inss, desconto_fgts,
                    total_de_descontos, salario_liquido))
    print('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')


