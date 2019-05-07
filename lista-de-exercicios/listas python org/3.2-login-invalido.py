print('\n\n>>>SIGN IN<<<')

nome = str(input('Insira o nome do usuário: ').upper())
senha = str(input('Insira a senha: ').upper())

while nome == senha:
    print('\n!ERRO! -> Usuário ou senha inválido\nTente novamente...')
    nome = str(input('\n\nInsira o nome do usuário: ').upper())
    senha = str(input('Insira a senha: ').upper())

else:
    print('\nUsuário registrado com SUCESSO.')