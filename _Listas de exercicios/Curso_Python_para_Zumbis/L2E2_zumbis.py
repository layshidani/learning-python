
# coding: utf-8

# # 2. Determine se um ano é bissexto.
# 
# ### Condições para o ano ser bissexto:
# 
# Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
# 
# Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
# 
# Pode ser que seja divisível por 400.

# In[ ]:


ano = int(input('Digite o ano que você deseja saber se é bissexto: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(':) Sim! {} é um ano BISSEXTO!'.format(ano))
else:
    print(':/ {} não é um ano bissexto...'.format(ano))
    
acerto = str(input('\nAcertamos??? (digite: sim ou não)').lower())
if acerto == 'sim':
	print('\nFicamos felizes em saber!')
elif acerto == 'não':
	print('\nAhh, que pena! onde será que erramos? ')

