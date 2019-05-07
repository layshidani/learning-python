print('''\n19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e
16''')

print('\nCENTENAS, DEZENAS e UNIDADES')
n = int(input('Informe um nº inteiro menor do que 1000: '))

c = n // 100
d = (n - c * 100) // 10
u = n - (c * 100) - (d * 10)

if c > 1:
    ext_c = 'centenas'
else:
    ext_c = 'centena'

if d > 1:
    ext_d = 'dezenas'
else:
    ext_d = 'dezena'

if u > 1:
    ext_u = 'unidades'
else:
    ext_u = 'unidade'

print('\n{} = {} {}, {} {} e {} {}' .format(n, c, ext_c, d, ext_d, u, ext_u))
