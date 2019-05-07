
# coding: utf-8

# In[3]:


import random

lista = []
while len(lista) < 15:
    x = random.randint(10,100)
    if x not in lista:
        lista.append(x)
lista.sort()
print(lista)
    

