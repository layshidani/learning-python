# exercicio inspirado no ex 7.4 do livro, porém feito modificações

# coding: utf-8

print('---' * 15)
print('Bem vindo(a) à Pizzaria Brasil')
print('---' * 15)

print('\nVamos montar seu pedido!\nOpções disponíveis: ')
print('''\t* Mussarela\n\t* Calabresa\n\t* Cebola\n\t* Champion\n\t* Bacon\n\t* Ovo\n\t* Alho\n\t* Presunto
\t* Manjeiricão\n\t* Brocolis\n\t* Milho\n\t* Oregano''')
print('\nAgora escolha um ingrediente de cada vez:\n'
      '**Digite \'quit\' a qualquer momento para sair ou encerrar o pedido')

ingredientes = []
ing_dispo = ['Mussarela', 'Calabreza', 'Cebola', 'Champion', 'Bacon', 'Manjericão', 'Brocolis', 'Milho', 'Ovo', 'Alho',
             'Presunto', 'Oregano']

ingrediente = str(input('\n\033[33;1;34mQual ingrediente deseja incluir na sua pizza?\033[m: ').title().strip())

while True:
    if ingrediente not in ing_dispo:
        print('\n\033[31m>>> Opa..Ingrediente indisponível.\033[m Tente outro: ')
        ingrediente = str(input('\n\033[33;1;34mQual ingrediente deseja incluir na sua pizza?\033[m: ').title().strip())
    else:
        ingredientes.append(ingrediente)
        print('\n\033[32m--> Os ingrentes que já estão na sua pizza são:\033[m ', ingredientes)
        ingrediente = str(input('\n\033[33;1;34mQual ingrediente deseja incluir na sua pizza?\033[m: ').title().strip())

    if ingrediente == 'Quit':
        print('\n\033[30;47mPedido finalizado.\033[m')
        print('\n\033[32m--> Os ingrentes da sua pizza são:\033[m ', ingredientes)
        break
