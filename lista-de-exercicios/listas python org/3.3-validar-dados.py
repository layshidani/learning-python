print('''\n\nParâmetros:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';''')

nome = str(input('\nInsira o nome: ').upper())
while nome.__len__() <= 3:
    print('\nInformação inválida. Tente novamente.')
    nome = str(input('\nInsira o nome: ').upper())

else:
    idade = int(input('Insira a idade: '))

while idade < 0 or idade > 150:
    print('\nInformação inválida. Tente novamente.')
    idade = int(input('Insira a idade: '))

else:
    salario = float(input('Informe o salário R$ '))

while salario < 0:
    print('\nInformação inválida. Tente novamente.')
    salario = float(input('Informe o salário R$ '))

else:
    sexo = str(input('Informe o sexo (F/M): ').upper())

while (sexo != 'F') and (sexo != 'M'):
    print('\nInformação inválida. Tente novamente.')
    sexo = str(input('Informe o sexo (f/m): ').upper())

else:
    estadocivil = str(input('Informe o estado civil (s/c/v/d): ').upper())
    lista = ['S', 'C', 'V', 'D']

while estadocivil not in lista:
    print('\nInformação inválida. Tente novamente.')
    estadocivil = str(input('Informe o estado civil (s/c/v/d): ').upper())

print('\n>>> Dados validados com SUCESSO! <<<')
