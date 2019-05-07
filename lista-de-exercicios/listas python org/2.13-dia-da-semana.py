print('''\n13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
outro valor deve aparecer valor inválido''')

n = int(input('''\nInforme um numero: 
                    1-Domingo, 
                    2-Segunda-feira,
                    3-Terça-feira,
                    4-Quarta-feira,
                    5-Quinta-feira,
                    6-Sexta-feira,
                    7-Sábado                    
                    '''))

if (n == 1):
    print('\nDomingo')
elif (n == 2):
    print('\nSegunda-feira')
elif (n == 3):
    print('\nTerça-feira')
elif (n == 4):
    print('\nQuarta-feira')
elif (n == 5):
    print('\nQuinta-feira')
elif (n == 6):
    print('\nSexta-feira')
elif (n == 7):
    print('\nSábado')
else:
    print('\nO número digitado é inválido! Tente outra vez...')

