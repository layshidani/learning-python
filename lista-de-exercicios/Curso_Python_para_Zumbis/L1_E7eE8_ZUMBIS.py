#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
c = float(input('Digite a temperatura em Celsius: '))
f = 9*(c/5)+32
print('\n{} ºC equivale a {} Fahrenheit' .format(c,f))

#Faça agora o contrário, de Fahrenheit para Celsius.
f = float(input('Digite a temperatura em Fahrenreit: '))
c = ((f - 32)/9)*5
print('\n{} Fahrenheit equivale a {} ºC. ' .format(f,c))
print('\n***FIM***')
