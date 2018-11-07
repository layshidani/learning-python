
# coding: utf-8

# ## 1.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# In[5]:


nota = float(input('Insira a nota do aluno: '))
while nota < 0 or nota > 10:
    print('\nERRO! A nota digitada é inválida. Tente novamente...')
    nota = float(input('Insira a nota do aluno: '))
else:
    print('\nA nota foi armazenada com sucesso! :D')

   

