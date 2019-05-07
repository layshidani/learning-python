print('\n18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.')

data_usu = str(input('\nInforme a data de hoje no formato dd/mm/aaaa: '))

dia = int(data_usu[0:2])
mes = int(data_usu[3:5])
ano = int(data_usu[6:])

if dia in range(1,31):
    dia_valido = 'SIM'
else:
    dia_valido = 'NÃO'

if mes in range(1, 12):
    mes_valido = 'SIM'
else:
    mes_valido = 'Não'

if ano = 2018:
    ano_valido = 'SIM'
else:
    ano_valido = 'NÃO'

if (dia_valido == 'SIM') and mes_valido == 'SIM' and ano_valido == 'SIM':
    print('\nA data {} inserida é válida!' .format(data_usu))
else:
    print('\nA data {} inserida é INVÁLIDA!!!!' .format(data_usu))
