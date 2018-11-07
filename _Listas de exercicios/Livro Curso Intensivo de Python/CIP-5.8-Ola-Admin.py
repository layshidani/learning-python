# coding: UTF-8
print('----' * 30)
print('Olá, usuário!')
print('----' * 30)

usuarios = ['admin', 'Cah', 'Juju', 'Rui', 'Valen']

for usuario in usuarios:
    if usuario == 'admin':
        print('\nOlá, Admin...Gostaria de ver um relatório de status?')
    else:
        print('\nOlá ' + usuario + '! Obrigado por fazer login novamente!')
