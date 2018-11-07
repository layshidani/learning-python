
# coding: utf-8

# # 1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# 

# ### Condição de existência de um triângulo

# Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados. Veja o resumo da regra abaixo: 
# 
# | b - c | < a < b + c 
# 
# | a - c | < b < a + c 
# 
# | a - b | < c < a + b 
# 
# #### Equilátero, isósceles ou escaleno
# 
# Triângulo equilátero: possui os três lados com medidas iguais.
# 
# Triângulo isósceles: possui dois lados com medidas iguais.
# 
# Triângulo escaleno: possui os três lados com medidas diferentes. 

# In[ ]:


a = float(input('Qual o valor de a? '))
b = float(input('Qual o valor de b? '))
c = float(input('Qual o valor de c? '))

if a > b + c or b > a + c or c > a + b:
    print('Não é um triângulo! Pois um dos lados é maior do que a soma dos outros dois.')
    
elif a == b == c:
    print('É um triângulo EQUILATERO!')
    
elif a == b or a == c or c == b:
    print('É um triângulo ISOSCELES!')

elif a != b or a != c or b != c:
    print('É um triângulo ESCALENO!')

