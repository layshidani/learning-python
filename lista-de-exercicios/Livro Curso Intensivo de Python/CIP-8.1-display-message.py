# coding: utf-8

print('---' * 20)
print('\033[2mO que estou aprendendo neste capítulo\033[m')
print('---' * 20)


def display_message(name):
    '''Mostra uma mensagem sobre o que estou aprendendo neste capítulo'''
    print('---' * 20)
    print('\nOlá, ' + name + '. Tudo bem?')
    print('Neste capítulo estou aprendendo a definir funções em Python.')


name = str(input('\nQual é o seu nome? ').title().strip())
display_message(name)
print('---' * 20)
