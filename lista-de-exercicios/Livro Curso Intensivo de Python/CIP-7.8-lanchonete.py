# coding: utf-8

print('---' * 15)
print('\033[2mBem vindo(a) à Lanchonete do Big Ozzy\033[m')
print('---' * 15)

sandwich_orders = ['x-bacon', 'x-egg', 'x-bacon', 'x-tudo', 'hotdog completo']
prep_sandwich = []
finished_sandwches = []

for sandwich in sandwich_orders:
    while sandwich_orders:
        current_sand = sandwich_orders.pop()
        print('\nEstamos Preparando: ' + current_sand)
        prep_sandwich.append(current_sand)

    print('---' * 15)
    print('\033[2mAguarde um instante... \033[m')
    print('---' * 15)

    while prep_sandwich:
        preparando = prep_sandwich.pop()
        print('\nPronto! Vai um' + '\t* ' + preparando + ' ... Quentinhooo!')
        finished_sandwches.append(preparando)
