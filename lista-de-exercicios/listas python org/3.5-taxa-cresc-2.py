print('\n>>> TAXA DE CRESCIMENTO POPULACIONAL <<<')

pop_a = float(input('\nInforme o total de habitantes do país A: '))
pop_b = float(input('\nInforme o total de habitantes do país B: '))
taxa_a = float(input('\nInforme a taxa de crescimento anual do país A: '))
taxa_b = float(input('\nInforme a taxa de crescimento anual do país B: '))
anos = 0

while pop_a <= pop_b:
    pop_a = pop_a + (pop_a * (taxa_a / 100))
    pop_b = pop_b + (pop_b * (taxa_b / 100))
    anos += 1

else:
    print('\nA taxa populacional foi igualada: ')
    print('Em {} anos.' .format(anos))
