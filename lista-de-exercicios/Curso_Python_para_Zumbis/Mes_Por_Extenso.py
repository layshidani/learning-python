
# coding: utf-8

# ## Informe o dia, o mês e o ano do seu nascimento no formato dd/mm/aaaa e imprima o mês por extenso. 

# In[11]:


dia, mês, ano = input('Informe o dia, o mês e o ano do seu nascimento no formato dd/mm/aaaa: ').split('/')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',          'agosto', 'setembro', 'outubro', 'novembro','dezembro']
print('Você nasceu em {} de {} de {}.'.format(dia,meses[int(mês)-1], ano))

