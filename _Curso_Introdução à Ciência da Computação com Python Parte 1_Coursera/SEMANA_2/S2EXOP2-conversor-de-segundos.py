# coding: UTF-8

print('---' * 30)
print('Entrada de Dados desafio: Conversor de segundos')
print('---' * 30)

segundos_ = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = segundos_ // 86400
segundos_restantes = segundos_ % 86400
horas = segundos_restantes // 3600
segundos_restantes = segundos_restantes % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos.')
print('---' * 30)
