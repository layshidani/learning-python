# coding: UTF-8

print('----' * 30)
print(':::' + 'Os 8 maiores rios do mundo' + ':::')
print('----' * 30)

rios = {
    'amazonas': 'américa do sul',
    'nilo': 'áfrica ocidental',
    'chang yian': 'china',
    'mississippi-missouri-red-rock': 'EUA',
    'yenisei': 'russia',
    'Ob-Irtish': 'russia',
    'Huang Ho (Amarelo)': 'china',
    'Heilong (Amur)': 'ásia'
    }

for rio, local in rios.items():
    print('\n#  Nome do rio: ' + rio.title() + '\n-> Localização: ' + local.title())

print('\nOs rios citados são:')
for nome in rios.keys():
    print('* ' + nome.title())

print('\nAs localizações citadas são:')
for local in rios.values():
    print('*' + local.title())

