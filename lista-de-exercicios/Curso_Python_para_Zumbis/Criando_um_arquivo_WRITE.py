
# coding: utf-8

# In[1]:


arquivo = open('numeros.txt', 'w')
for linha in range(1, 101):
    arquivo.write('\n{}'.format(linha))
arquivo.close()

