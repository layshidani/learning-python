print('''8. Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.''')

print('\nVamos calcular seu salário!')
h = float(input('\nInforme quantas horas você trabalha por dia: '))
d = int(input('Informe quantos dias por semana você trabalha: '))
sh = float(input('Informe quanto você ganha por hora trabalhada R$: '))
dm = d * 4
hm = h * dm
salario = sh * hm

print('\n>>> Você trabalha em um mês: \n{} horas \n{} dias' .format(hm, dm))
print('\n>>> Seu salário mensal é de R$ {:.2f}' .format(salario))