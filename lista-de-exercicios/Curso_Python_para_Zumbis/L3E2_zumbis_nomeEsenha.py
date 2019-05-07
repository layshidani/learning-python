
# coding: utf-8

# ## 2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

# In[2]:


print('***REGISTRO***')
nome = str(input('Digite um nome de usuário: '))
senha = str(input('Digite uma senha: '))
while nome.lower() == senha.lower():
    print('\n ERRO! A senha deve ser diferente do nome de usuário..Tente novamente!')
    nome = str(input('Digite um nome de usuário: '))
    senha = str(input('Digite uma senha: '))
else:
    print('Usuário cadastrado com sucesso!')

