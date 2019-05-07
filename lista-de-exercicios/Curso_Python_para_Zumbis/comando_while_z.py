n1 = float(input('Insira um número: '))
n2 = float(input('Insira mais um número: '))
n3 = float(input('Insira mais um número: '))

if n1 <= n2 and n1 <= n3:
	print('\nNós analisamos seus números e descobrimos que {:.1f} é o menor deles!'.format(n1))
elif n2 <= n1 and n2 <= n3:
	print('Nós analisamos seus números e descobrimos que {:.1f} é o menor deles!'.format(n2))
else:
	print('Nós analisamos seus números e descobrimos que {:.1f} é o menor deles!'.format(n3))

acerto = str(input('\nAcertamos??? (digite: sim ou não)').lower())
if acerto == 'sim':
	print('\nFicamos felizes em saber!')
elif acerto == 'não':
	print('\nAhh, que pena! onde será que erramos? ')