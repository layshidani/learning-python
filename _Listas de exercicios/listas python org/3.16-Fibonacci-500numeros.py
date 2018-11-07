print('---' * 20)
print('Sequência Fibonacci')
print('---' * 20)

n1 = 0
n2 = 1
cont = 0

while cont < 100:
    n3 = n1 + n2
    cont += 1
    print(n3, end=' -> ')
    n1 = n2
    n2 = n3
    if n2 > 500:
        break

print('\n\n***FIM***')