print("-=-" * 20)
print("Vamos contar números primos!!!")
print("-=-" * 20)
 

def n_primos(n):
    primos = []
    for num in range(n + 1):
        i = 0
        for divisor in range(n + 1):
            if num % (divisor + 1) == 0 and num != divisor:
                i += 1
        if i == 2:
            primos.append(num)
    print(len(primos))


n = int(input('Digite um nº natural maior ou igual a 2: '))

while n < 2:
    n = int(input('Digite um nº natural maior ou igual a 2: '))

n_primos(n)

