# coding: UTF-8

print('----' * 15)
print(':::' + 'Os 3 maiores rios do mundo' + ':::')
print('----' * 15)

rios = {
    'amazonas': {'local': 'américa do sul', 'tamanho': '6.868'},
    'nilo': {'local': 'áfrica ocidental', 'tamanho': '6.695'},
    'chang yian': {'local': 'china', 'tamanho': '6.380'}
    }

for rio, rio_info in rios.items():
    local = rio_info['local'].title()
    tamanho = rio_info['tamanho']
    print('\n:::' + rio.title() + ':::')
    print('*Localização: ' + local)
    print('*Tamanho: ' + tamanho + ' km')
