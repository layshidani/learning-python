print('\n>>> Soma e Média de uma sequência de 5 números <<<')

lista = []
n1 = lista.append(float(input('\nInforme um nº: ')))
n2 = lista.append(float(input('Informe um nº: ')))
n3 = lista.append(float(input('Informe um nº: ')))
n4 = lista.append(float(input('Informe um nº: ')))
n5 = lista.append(float(input('Informe um nº: ')))

print('\n\n---> Sequência: {}' .format(lista))
print('-----> Soma da sequência = {}' .format(sum(lista)))
print('--------> Média da sequência = {}' .format(sum(lista) / len(lista)))
