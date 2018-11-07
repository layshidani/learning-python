print('L1_E5_Zumbis \n====Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar=====')
psd = float(input('Insira o preço do produto: R$ '))
dsc = float(input('Insira o percentual de desconto: % '))
vdsc = psd*(dsc/100)
pcd = psd-vdsc

print('\n O valor do desconto é: R$ ', vdsc)
print('O valor final a pagar é: R$ ', pcd)


print('\n***FIM***')