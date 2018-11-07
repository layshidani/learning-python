print('\n >>> Números inteiros entre sequência e soma <<<')

n1 = int(input('Informe o primeiro nº do intervalo: '))
n2 = int(input('Informe o último nº do intervalo: '))

lista = [n1]

while n1 < n2:
    n1 += 1
    lista.append(n1)

print('\nSequência gerada pelos nº informados:')
print(lista)
print('\nSoma dos nº da sequência: {} ' .format(sum(lista)))