# coding: utf-8

print('---' * 15)
print('Lugares Favoritos')
print('---' * 15)

favorite_places = {
    'Manu': ['Cozinha', 'sofá'],
    'Ozzy': ['sapateira', 'quarto'],
    'Rui': ['banheiro', 'quarto'],
    'Valentina': ['sala', 'quarto']
    }

for name, places in favorite_places.items():
    print('\nNome: ' + name)
    print('Lugares favoritos:')
    for place in places:
        print('* ' + place)
