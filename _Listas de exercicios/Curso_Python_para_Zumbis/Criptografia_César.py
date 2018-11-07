
# coding: utf-8

# In[23]:


print('***Criptografia de Mensagens***')

def esconde(msg):
    s = ''
    for c in msg:
        s += chr(ord(c) + 30000)
    return s
def mostra(msg):
    s = ''
    for c in msg:
        s += chr(ord(c) - 30000)
    return s

print(esconde('Olá mundo!'))

print(mostra('畿疜瘑畐疝疥疞疔疟畑'))

