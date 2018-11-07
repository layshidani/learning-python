print('Conta de Telefone\n')

# m=float(input('Insira a quantidade de minutos ultilizados: '))
# if m < 200:
#    p = 0.20
# else:
#    if m <=400:
#        p = 0.18
#    else:
#        if m<=800:
#            p = 0.15
#       else:
#            p=0.08

# print('O valor da conta é R$ {}' .format(p*m))

# ou usar a nova função elif


m2=float(input('Insira a quantidade de minutos ultilizados: '))

if m2 < 200:
    p2 = 0.20
elif m2 <= 400:
    p2 = 0.18
elif m2 <= 800:
    p2 = 0.15
else:
    p2 = 0.08

print('O valor da conta é R$ {:.2f}'.format(p2*m2))

print('***FIM***')
