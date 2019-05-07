print('== Desafio 003 - Guanabara - Curso em vídeo ==')
print('\n==Iserir 2 números e depois exibir a soma==')

n1=int(input('\nDigite um nº: '))
n2=int(input('\nDigite um nº: '))

s=n1+n2

print('\nModo 1 - Antigo')
print(n1,'+',n2,' = ', s, '  ---->  ','A soma é igual a: ',s)
print('\nModo 2')
print('{}'' + ''{}'' = ' '{}' .format(n1, n2, s),  '  ---->  ','A soma é igual a: {}'.format(s))

print('\n==Fim do Desafio 003==')
