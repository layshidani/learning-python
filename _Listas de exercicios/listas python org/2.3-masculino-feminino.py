print('''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M -
Masculino, Sexo Inválido.''')

sexo = str(input('Olá, Informe F para feminino ou M para masculino: ')).upper()
if sexo == 'F':
    print('Sexo Feminino')
elif sexo == 'M':
    print('Sexo masculino')
else:
    print('Sexo inválido')