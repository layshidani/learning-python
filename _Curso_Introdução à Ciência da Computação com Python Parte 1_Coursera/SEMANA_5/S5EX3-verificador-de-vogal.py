# coding: utf-8

print('-=-' * 25)
print('Verificador de Vogais')
print('-=-' * 25)


def vogal(caracter):
	if caracter in ('aeiouáéíóúâêôãõAEIOUÁÉÍÓÚÂÊÔÃÕ'):
		eh_vogal = True
		return eh_vogal
	else:
		eh_vogal = False
		return eh_vogal


caracter = str(input('Informe caracter, nós iremos analisar se ele é uma vogal ou não: ').lower())

vogal(caracter)
