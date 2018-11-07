
# coding: utf-8

# In[13]:


def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True
     
arquivo = open('Validador_de_IPs.txt', 'r')
validos = open('Validador_de_IPs_validos.txt', 'w')
invalidos = open('Validador_de_IPs_invalidos.txt', 'w')

for linha in arquivo.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)

arquivo.close()
validos.close()
invalidos.close()
        

