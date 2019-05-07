# coding: utf-8

print('''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
\n– O nome com todas as letras maiúsculas e minúsculas;
\n– Quantas letras ao todo (sem considerar espaços);
\n– Quantas letras tem o primeiro nome.
\nVamos analisar o seu nome!''')

nome = str(input('Digite seu nome completo: ').title()).strip()

print('Seu nome com todas as letras maiúsculas é: ', nome.upper())
print('Seu nome com todas as letras minúsculas é: ', nome.lower())
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))

#Há 2 formas de resolver a próxima linha de comando:
s = nome.split()

#1 utilizando find(' '), pois o programa irá procurar o primeiro espaço entre um nome e outro
#e retornar essa posição, que é o mesmo que contar a quantidade de caractéres do primeiro nome
print('Seu primeiro nome é {} e ele tem {} letras'.format(s[0], nome.find(' ')))

#2 utilizando o comando len
print('Seu primeiro nome é {} e ele tem {} letras'.format(s[0], len(s[0])))
