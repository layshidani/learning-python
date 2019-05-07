# coding: UTF-8
print('----' * 30)
print('Números ordinais por extenso')
print('----' * 30)

for numero in range(1, 10):
    if numero == 1:
        print(str(numero) + 'st')
    elif numero == 2:
        print(str(numero) + 'nd')
    elif numero == 3:
        print(str(numero) +'rd')
    else:
        print(str(numero) + 'th')
