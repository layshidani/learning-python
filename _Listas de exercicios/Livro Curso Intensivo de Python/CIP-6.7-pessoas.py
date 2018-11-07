# coding: UTF-8
print('----' * 30)
print('Dados sobre uma pessoa')
print('----' * 30)

pessoas = []

pessoa = {
    'first_name': 'June',
    'last_name': 'Hidani',
    'age': '7',
    'city': 'Ferraz de Vasconcelos'
    }

pessoas.append(pessoa)

pessoa = {
    'first_name': 'Lays',
    'last_name': 'Hidani',
    'age': '28',
    'city': 'Ferraz de Vasconcelos'
    }

pessoas.append(pessoa)

for pessoa in pessoas:
    print('\nDados sobre a pessoa analisada: \n\t' + 'Nome: '
      + pessoa['first_name'].title() + ' ' + pessoa['last_name'].title())
    print('\tIdade: ' + pessoa['age'] + ' anos')
    print('\t' + 'Cidade: ' + pessoa['city'].title() + '.')