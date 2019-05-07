#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão

c = str(2**1000000000)
print(len(c))

#ou
print(len(str(2**1000000000)))



