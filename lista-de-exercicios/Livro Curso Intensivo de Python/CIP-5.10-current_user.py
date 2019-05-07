# coding: UTF-8
print('----' * 30)
print('Verificador de nome de usuário')
print('----' * 30)

current_users = ['Cah', 'Valen', 'Rui', 'June', 'Admin']
new_users = []

while True:
    new_users.append(str(input('\nEscolha um nome de usuário: ')))

    for user in new_users:
        if user.title() in current_users:
            print('\nEste nome de usuário já está sendo usado por outra pessoa.\nTente um diferente...')
            new_users.append(str(input('\nEscolha um nome de usuário: ')))
        else:
            print('\nNome de usuário cadastrado com sucesso!')

    break







