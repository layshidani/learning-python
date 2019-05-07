
# coding: utf-8

# ## 7 . Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

# In[12]:


a = float(input('Informe a área em m² a ser pintada: '))
from math import trunc
litros = (a / 3)
round(litros)
latas = (litros / 18)
if latas < 1:
    latas_int = 1
else:
    latas_int = round(latas)

preco = latas_int * 80

print('Para pintar {:.2f} m², serão necessárias {:.2f} lata(s) de tinta 18l.'.format(a, latas_int))
print('O valor total para comprar {:.2f} lata(s) é R$ {:.2f}.'.format(latas_int, preco))

