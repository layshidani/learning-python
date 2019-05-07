
# coding: utf-8

# ## 3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.

# In[2]:


peso = float(input('Olá! Quantos kilos de peixe você pescou hoje? '))
if peso <= 50:
    print('Parabéns! Não há multa a pagar :D')
else:
    excesso = peso - 50
    multa = excesso * 4
    print(':/ Houve um excesso de {:.3f} kg'.format(excesso))
    print('Portanto, há uma multa no valor de R$ {:.2f}'.format(multa))

