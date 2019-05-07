print('''10.Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
conforme o caso.''')

turno = str(input('Em qual turno você estuda??? Digite M-matutino ou V-Vespertino ou N- Noturno:  ')).upper()

if turno == 'M':
    print('\nBom dia!')
elif turno == 'V':
    print('\nBoa tarde!')
else:
    print('\nBoa noite!')