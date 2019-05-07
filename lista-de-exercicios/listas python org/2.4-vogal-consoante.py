print('''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.''')

def vogal(letra):
    vogais = "aeiou"
    if letra.lower() not in vogais: # verificar se a letra digitada minuscula nao existe na nossa variavel vogais
        return 'Não é vogal'
    return 'Sim, é uma vogal!'

letra = input("\nDigite uma letra: ")
print(vogal(letra))
