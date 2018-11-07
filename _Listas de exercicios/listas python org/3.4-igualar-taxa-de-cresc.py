print('\n>>> TAXA DE CRESCIMENTO POPULACIONAL <<<')

pop_a = 80000
pop_b = 200000
taxa_a = 3 / 100
taxa_b = 1.5 / 100
anos = 0

while pop_a <= pop_b:
    pop_a = pop_a + (pop_a * taxa_a)
    pop_b = pop_b + (pop_b * taxa_b)
    anos += 1

else:
    print('\nA taxa populacional foi igualada: ')
    print('Em {} anos.' .format(anos))

