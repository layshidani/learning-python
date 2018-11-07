
# coding: utf-8

# In[ ]:


#Criado por Lays Marie Hidani
import random
print('ATENÇÃO!!! Bem-vindo(a) aos números da sorte da Mega-Sena\n***Vamos sortear alguns números para você apostar!***')

lista = []
while len(lista) < 6:
    x = random.randint(1,61)
    if x not in lista:
        lista.append(x)
lista.sort()
    
    

comecar = str(print(input('\nDigite ESTOU COM SORTE para começar: ').upper()))

if comecar == 'ESTOU COM SORTE':
    print('\n\nOs números escolhidos são: {}'.format(lista))
else:
    print('Tente de novo')

