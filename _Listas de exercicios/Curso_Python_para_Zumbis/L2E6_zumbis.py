
# coding: utf-8

# ## 6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# 
# a. + Salário Bruto : R$
# 
# b. - IR (11%) : R$
# 
# c. - INSS (8%) : R$
# 
# d. - Sindicato ( 5%) : R$
# 
# e. = Salário Liquido : R$

# In[2]:


s_bruto = float(input('Informe o valor de seu salário bruto: R$ '))
ir = s_bruto * 0.11
inss = s_bruto * 0.08
sindic = s_bruto * 0.05
desc = ir + inss + sindic
s_liq = s_bruto - desc
print('O total das taxas pagas é R$ {:.2f}'.format(desc))
print('Sendo:\nIR: R$ {:.2f}, \nINSS: R$ {:.2f}, \nSindicato: R$ {:.2f}'.format(ir, inss, sindic))
print('\nO valor de seu salário líquido é: R$ {:.2f}'.format(s_liq))

