print('''\nExercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de 
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.''')

from random import shuffle

aluno_1 = str(input('\nInforme o nome do aluno 1: '))
aluno_2 = str(input('Informe o nome do aluno 2: '))
aluno_3 = str(input('Informe o nome do aluno 3: '))
aluno_4 = str(input('Informe o nome do aluno 4: '))

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

print('\nA ordem de apresentação sorteada é: ')
shuffle(lista)
print(lista)