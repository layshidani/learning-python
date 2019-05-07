
# coding: utf-8

# ### Modo 1: Programadores normais

# In[2]:


arquivo = open('numeros.txt','r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()


# ### Modo 2: Modo Pythonico

# In[3]:


with open('numeros.txt') as n:
    print(n.read())

