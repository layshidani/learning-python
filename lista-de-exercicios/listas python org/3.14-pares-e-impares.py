
print('===' * 20)
print('\nVamos verificar quais são os nº pares e impares de 10 nº escolhidos por você..')

lista_num = []
lista_pares = []
lista_impares = []

while len(lista_num) < 10:
    num = lista_num.append(int(input('\nInsira um nº: ')))

for x in lista_num:
    if (x % 2) == 0:
        lista_pares.append(x)
    else:
        lista_impares.append(x)

print('\nNº escolhidos pelo usuário: {}' .format(lista_num))
print('\nNúmeros pares da lista: {}' .format(lista_pares))
print('\nNúmeros impares da lista: {}' .format(lista_impares))

print('===' * 20)
