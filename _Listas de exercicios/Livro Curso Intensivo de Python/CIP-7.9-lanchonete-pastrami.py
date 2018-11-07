# coding: utf-8

print('---' * 15)
print('\033[2mBem vindo(a) à Lanchonete do Big Ozzy\033[m')
print('---' * 15)

print('\n!Informamos que no momento estamos sem pastrami. Agradecemos a compreensão!')

sandwich_orders = ['x-bacon', 'pastrami', 'x-egg', 'pastrami', 'x-bacon', 'x-tudo', 'hotdog completo', 'pastrami']
prep_sandwich = []
finished_sandwches = []

while 'pastrami' in sandwich_orders:
    print('Infelizmente não temos pastrami. Pedido cancelado.')
    print('Pedido nº: ', sandwich_orders.index('pastrami'))
    pastrame_nao = sandwich_orders.remove('pastrami')

print('---' * 15)

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
        print('\nPronto! Aqui vai um' + '\t* ' + preparando + ' ... Quentinhooo!')
        finished_sandwches.append(preparando)
