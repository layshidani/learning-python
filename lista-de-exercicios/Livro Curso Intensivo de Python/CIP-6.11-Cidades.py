# coding: utf-8

print('---' * 15)
print('Info sobre cidades')
print('---' * 15)

cidades = {
    'são paulo': {
        'estado': 'são paulo',
        'prefeito atual': 'bruno covas',
        'população': '13.11 milhões'
        },
    'curitiba': {
        'estado': 'paraná',
        'prefeito atual': 'Rafael Greca',
        'população': '1,765 milhão'
        }
    }

for cidade, infos in cidades.items():
    print('\nNome do município: ' + cidade.title())
    print(' * Estado: ' + infos['estado'].title())
    print(' * Prefeito atual: ' + infos['prefeito atual'].title())
    print(' * População: ' + infos['população'])


