
# coding: utf-8

# In[7]:


notas = []
soma = 0
i = 1
while i <= 4:
    n = float(input('Insira a nota: '))
    notas.append(n)
    soma += n
    i += 1
print('Notas: ', notas)
print('A média final é {:.2f}'.format(soma/4))


# 
# 
# 
