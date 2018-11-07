print('4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.')

print('\nVamos calcular a nota média do aluno: ')
print('\nAtenção use . ao invés de ,')

n1 = float(input('\nInsira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))
n4 = float(input('Insira a quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

print('A média final do aluno é: {:.2f}' .format(media))