
# coding: utf-8

# ## Gere uma lista de 15 números inteiros de uma lista de 10 a 100
# 

# In[77]:


import random

lista = []
for k in range(15):
    lista.append(random.randint(10,100))
print(lista)

