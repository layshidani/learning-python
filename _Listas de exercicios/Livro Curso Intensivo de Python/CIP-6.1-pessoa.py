# coding: UTF-8
print('----' * 30)
print('Dados sobre uma pessoa')
print('----' * 30)

dados = {
    'first_name': 'June',
    'last_name': 'Hidani',
    'age': '7',
    'city': 'Ferraz de Vasconcelos'
    }

print('\nO nome completo da pessoa analisada é: \n\t'
      + dados['first_name'].title() + ' ' + dados['last_name'].title())

print('\tIdade: ' + dados['age'] + 'anos')
print('\t' + dados['first_name'] + ' Cidade: ' + dados['city'].title() + '.')
