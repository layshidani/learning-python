# coding: utf-8

#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto 
#e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('\nPara um triângulo de CO = {:.2f} e CA = {:.2f}, \nO valor de hipotenusa é H = {:.2f}'.format(co, ca, hi))


# In[10]:


#outro método com import
from math import hypot
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hi = hypot(co, ca)
print('\nPara um triângulo de CO = {:.2f} e CA = {:.2f}, \nO valor de hipotenusa é H = {:.2f}'.format(co, ca, hi))

