print('''\nFaça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
***O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.''')

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
n1 = float(input('Insira a primeira nota parcial do aluno: '))
n2 = float(input('Insira a segunda nota parcial do aluno: '))

media = (n1 + n2) / 2

if (9.0 <= media < 10.0):
    print('\nAluno - Conceito A >>> APROVADO')
    print('Média:', media)
elif (7.5 <= media < 9.0):
    print('\nAluno - Conceito B >>> APROVADO')
    print('Média:', media)
elif (6.0 <= media < 7.5):
    print('\nAluno - Conceito C >>> APROVADO')
    print('Média:', media)
elif (4.0 <= media < 6.0):
    print('\nAluno - Conceito D >>> REPROVADO')
    print('Média:', media)
elif (media < 4.0):
    print('\nAluno - Conceito E >>> REPROVADO')
    print('Média:', media)