# coding: UTF-8
print('----' * 30)
print('Glossário de programação'.center(30, ':'))
print('----' * 30)

glossario = {
    'string': 'Sequência linear de caracteres. Itens são acessados via índice'
              '\n>>> Ex: \'Isso é uma string\'\n',
    'lista': 'Sequência linear de valores (elementos) que podem ser de qualquer e de diferentes tipos ' 
             '\n(listas, strings, inteiros, etc). Itens são acessados via índice'
             '\n>>>Ex: lista = [elemento1, elemento2, elemento3]\n',
    'tupla': 'Sequência linear de valores (elementos) que podem ser de qualquer e de diferentes tipos ' 
             '\nPorém, diferentemente das listas, são imutáveis!'
             '\n>>>Ex: tupla = (elemento1, elemento2, elemento3)\n',
    'range': 'Intervalo sequenciado de números inteiros. O índice começa em 0, por isso o último nº \nnão entra na '
             'sequência \n>>>Ex: range(0,11) irá criar um intervalo de 0 a 10\n',
    'dicionario': 'Coleção associativa desordenada. O valor é acessado por uma **chave** imutável '
                  'e não por indice\n>>>Ex: dicionário = {chave1: valor1, chave2: valor2}'
    }

word = ':::String:::'
print(word + '\nSignificado -> ' + glossario['string'])

word = ':::Lista:::'
print(word + '\nSignificado -> ' + glossario['lista'])

word = ':::Tupla:::'
print(word + '\nSignificado -> ' + glossario['tupla'])

word = ':::Range:::'
print(word + '\nSignificado -> ' + glossario['range'])

word = ':::Dicionário:::'
print(word + '\nSignificado -> ' + glossario['dicionario'])

print('----' * 30)
