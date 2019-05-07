# coding: UTF-8

print('---' * 20)
print('Mensagem Fatura')
print('---' * 20)

nome = str(input('Digite o nome do cliente: ').title())
dia_venc = str(input('Digite o dia de vencimento: '))
mes_venc = str(input('Digite o mês de vencimento: '))
valor = str(input('Digite o valor da fatura: '))


print('\nOlá, ' + nome)
print('A sua fatura com vencimento em ' + dia_venc + ' de ' + mes_venc + ' no valor de R$ ' + valor + ' está fechada.')

