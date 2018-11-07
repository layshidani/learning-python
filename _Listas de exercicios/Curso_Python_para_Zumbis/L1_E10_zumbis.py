#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros
# fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
print('Redução do tempo de vida de um fumante:')

a = int(input('\nInforme há quantos anos é fumante: '))
c = int(input('Informe quantos cigarros são fumados por dia: '))

tc = c*365*a
t = tc/144
print('\nCom base nos dados informados, \ncalcula-se que a pessoa pode ter uma redução de ', t, ' dias de vida por conta do cigarro.')



