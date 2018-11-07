#20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
#e presentar:
#a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#c. A mensagem "Aprovado com Distinção", se a média for igual a 10.

print('===' * 21)
print('Calculadora de média do aluno')
n1 = float(input('Insira a 1ª nota do aluno: '))
n2 = float(input('Insira a 2ª nota do aluno: '))
n3 = float(input('Insira a 3ª nota do aluno: '))

media = (n1 + n2 + n3) / 3

if media >= 7 and media != 10:
    print('Média: {} \n >>>APROVADO!<<<' .format(media))
elif media < 7:
    print('Média: {} \n >>>REPROVADO!<<<' .format(media))
elif media == 10:
    print('Média: {} \n >>>APROVADO COM DISTINÇÃO!<<<' .format(media))

print('===' * 21)
