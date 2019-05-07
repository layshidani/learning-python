# coding: UTF-8

pets = []

ozzy = {
    'nome': 'Ozzy',
    'tipo':  'felino',
    'cor': 'tigrado e branco',
    'dono(a)': 'leticia'
    }

pets.append(ozzy)

breno = {
    'nome': 'Breno',
    'tipo':  'felino',
    'cor': 'marrom claro',
    'dono(a)': 'Lays'
    }

pets.append(breno)

june = {
    'nome': 'June',
    'tipo':  'felino',
    'cor': 'cinza e branco',
    'dono(a)': 'Margareth'
    }

pets.append(june)

for pet in pets:
    nome = pet['nome'].title()
    tipo = pet['tipo'].title()
    cor = pet['cor'].title()
    dono = pet['dono(a)'].title()
    print('\n::::::: Dados do pet ::::::::')
    print('Nome: ' + nome)
    print('Tipo: ' + tipo)
    print('Cor: ' + cor)
    print('Dono: ' + dono)
    print(':::' * 10)