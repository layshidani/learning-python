
# coding: utf-8

# ### Leia uma mensagem.txt e grave cripto.txt, trocando todas as vogais por '*'

# In[20]:


texto = open('mensagem.txt')
saida = open('cripto.txt', 'w')

for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiouáéíóúãõ':
            saida.write('*')
        else:
            saida.write(letra)

texto.close()
saida.close()

