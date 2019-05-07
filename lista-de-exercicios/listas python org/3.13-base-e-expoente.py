print('===' * 20)
print('Vamos calcular exponenciação: base ^ expoente')

base = int(input('\nInforme o valor da base: '))
expo = int(input('Informe o valor do expoente: '))

n = 1
for num in range(1, expo + 1):
    n *= base

print('\nResultado:\n{} ^ {} = {:,}' .format(base, expo, n))
print('===' * 20)
