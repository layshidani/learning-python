
# coding: utf-8

# ## Defina uma função "embaralha", que retorne as letras de uma string misturadas
# 

# In[21]:


import random
def embaralha (s):
    lista = list(s)
    random.shuffle(lista)
    return ''.join(lista)

s = input('Digite uma palavra: ')
print('A palavra embaralhada fica: {}!'.format(embaralha(s)))

