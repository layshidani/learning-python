# 2.25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
# como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print(str('>>>><<<' * 10))
print(str(input('>>>Dpto de Policia de Ferraz<<< \nTecle <ENTER> para começar.')))
nome = str(input('\n_Informe o nome do suspeito interrogado: ').upper())
telefonou = str(input('\n\n_Informe se o suspeito telefonou para a vítima (s/n): ').upper())
local = str(input('_Informe se o suspeito Esteve no local do crime: (s/n): ').upper())
mora = str(input('_Informe se o suspeito mora próximo à vítima (s/n): ').upper())
deve = str(input('_Informe se o suspeito devia à vítima (s/n): ').upper())
trabalho = str(input('_Informe se o suspeito Já trabalhou com a vítima(s/n): ').upper())

lista = [telefonou, local, mora, deve, trabalho]

positivo = lista.count('S')

print('\n>>>Análise realizada com sucesso!<<<')

if positivo == 2:
    print('\nQtde de positivos: {}.\n{}: SUSPEITO (A)' .format(positivo, nome))
elif 3 <= positivo <= 4:
    print('\nQtde de positivos: {}. \n{}: CUMPLICE' .format(positivo, nome))
elif positivo == 5:
    print('\nQtde de positivos: {}.\n{}: CULPADO' .format(positivo, nome))
else:
    print('\nQtde de positivos: {}.\n{}: INOCENTE' .format(positivo, nome))

print(str('>>>><<<' * 10))
