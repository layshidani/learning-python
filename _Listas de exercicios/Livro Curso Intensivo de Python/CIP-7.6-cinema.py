# coding: utf-8

print('---' * 15)
print('\033[2mBem vindo(a) ao Cine Brasil\033[m')
print('---' * 15)

nome = str(input('\nQual o seu nome? '))

print('\nOlá, ' + nome.title() + '! Vamos calcular o valor dos ingressos...')

quantidade = int(input('\nInforme a quantidade de ingressos que deseja adquirir: '))

ingressos = []

idades = []

print('\n>>> Digite um a um a idade das pessoas que usarão os ingressos <<<')

for qtd in range(1, quantidade + 1):
    idade = int(input('\nInforme a idade: '))
    idades.append(idade)
    print('\n\033[32mIdades já adicionadas: {}\033[m' .format(idades))

for idade in idades:
    if idade <= 3:
        ingresso = 0
        ingressos.append(ingresso)
    elif 3 < idade < 12:
        ingresso = 10.0
        ingressos.append(ingresso)
    elif idade > 12:
        ingresso = 15.0
        ingressos.append(ingresso)

total = sum(ingressos)

print('\n\033[34m:::Ingressos contratados:::\033[m')
print('\t\033[1;34m* Idades: \033[m', idades)
print('\t\033[1;34m* Preço por idade: \033[m', ingressos)
print('\033[1;34m--> Preço total: R$ \033[m', total)
