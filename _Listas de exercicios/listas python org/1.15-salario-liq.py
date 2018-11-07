#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que
# são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
#a. salário bruto.
#b. quanto pagou de IR e ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.
#e. calcule os descontos e o salário líquido,

print('Olá, vamos calcular seu salário líquido mensal!')
valor_hora = float(input('Informe, quanto você ganha por hora trabalhada? R$ '))
horas = float(input('Informe quantas horas você trabalhou esse mês: '))

bruto = valor_hora * horas

ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05

descontos = ir + inss + sindicato
liquido = bruto - descontos

print('\nVeja os descontos que insidem sobre seu salário: '
      '\nR$ {:.2f} de Imposto de Renda'
      '\nR$ {:.2f} de INSS'
      '\nR$ {:.2f} de sindicato'
      '\n\nTotal de descontos R$ {:.2f}' .format(ir, inss, sindicato, descontos))
print('\n\nSeu salário bruto é de R$ {:.2f}'
      '\n Seu salário líquido é de R$ {:.2f}' .format(bruto, liquido))
