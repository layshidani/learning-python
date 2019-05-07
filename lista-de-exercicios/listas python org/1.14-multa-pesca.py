print('''14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
adequadas.''')

peso = float(input('\nOlá, quantos kilos de peixe você pescou hoje? '))
if (peso <= 50):
    print('\nNão há peso excedente, \nPortanto não há multa a ser paga hoje \n:D')
else:
    excesso = peso - 50
    multa = excesso * 4
    print('\nHoje você pescou {:.2f} kg acima do limite (50 kg)'
          '\nPortanto, foi gerada uma multa no valor de'
          '\nR$ {:.2f}' .format(excesso, multa))
    print('\nBom descanso!'
          '\nAté amanhã!')

