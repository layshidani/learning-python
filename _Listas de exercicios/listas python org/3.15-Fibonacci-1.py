print('---' * 20)
print('Sequência Fibonacci')
print('---' * 20)

n = int(input('Quantos números da sequência Fibonacci você quer ver? '))

n1 = 0
n2 = 1
cont = 0

while cont < n:
    n3 = n1 + n2
    cont += 1
    print(n3, end=' -> ')
    n1 = n2
    n2 = n3

print('\n\n***FIM***')