print('''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.''')

nome = str(input('\n\nInforme o nome do aluno: '))

notas = []
n1 = notas.append(float(input('Informe a primeira nota parcial do aluno: ')))
n2 = notas.append(float(input('Informe a segunda nota parcial do aluno: ')))

media = sum(notas) / len(notas)

if media >= 7 and media != 10:
    print('\nO aluno {}, teve média {:.2f}\nSituação: APROVADO! :)' .format(nome, media))
elif media < 7:
    print('\nO aluno {}, teve média {:.2f}\nSituação: REPROVADO! :/' .format(nome, media))
elif media == 10:
    print('\nParabéns, aluno NOTA 10!!! :D')

