import re


def le_assinatura():
    '''A funcao lê os valores dos traços linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    return (sum([abs(x - y) for x, y in zip(as_a, as_b)]) / len(as_b))


def calcula_assinatura(texto):
    sentencias = separa_sentencas(texto)

    frases = []
    for sentencia in sentencias:
        frases.append(separa_frases(sentencia))

    frases2 = [j for i in frases for j in i]
    palavras2 = []
    for frase in frases2:
        palavras2.append(
            separa_palavras(frase))  # palavras2 permite calcular exatamente a quantidade de palavras sem signos
    palavras2 = [j for i in palavras2 for j in i]  # Reorganizamos a lista de palavras2
    # outra opção para calcular palavras no texto
    palavras = separa_palavras(texto)

    # Calcular a assinatura *************************
    ass = []
    # 1) Tamanho médio de palavra: é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    soma_carateres_palavra = 0
    for palavra in palavras2:
        soma_carateres_palavra += len(palavra)
    ass.append(soma_carateres_palavra / len(palavras2))

    # 2) Relação Type-Token: é o número de palavras diferentes dividido pelo número total de palavras.
    #    Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente
    #    4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 4/5=0.8
    diferentes = n_palavras_diferentes(palavras2)
    ass.append(diferentes / len(palavras2))

    # 3) Razão Hapax Legomana: é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
    #    Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente
    #    3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 3/5=0.6
    unicas = n_palavras_unicas(palavras2)
    ass.append(unicas / len(palavras2))

    # 4) Tamanho médio de sentença: é a soma dos números de caracteres em todas as sentenças dividida pelo número de
    #    sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença)
    soma_carateres_sentencia = 0
    for sentencia in sentencias:
        soma_carateres_sentencia += len(sentencia)
    ass.append(soma_carateres_sentencia / len(sentencias))

    # 5) Complexidade de sentença: é o número total de frases divido pelo número de sentenças.
    ass.append(len(frases2) / len(sentencias))

    # 6) Tamanho médio de frase: é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
    #    (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
    soma_carateres_frase = 0
    for frase in frases2:
        soma_carateres_frase += len(frase)
    ass.append(soma_carateres_frase / len(frases2))

    # Retornar a assinatura do texto: ass
    return ass


def avalia_textos(textos, ass_cp):
    assinaturas = []
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        assinaturas.append(ass_texto)

    cohpiah = []
    for assinatura in assinaturas:
        cohpiah.append(compara_assinatura(assinatura, ass_cp))

    return cohpiah.index(min(cohpiah)) + 1


# Inicia o programa
ass_cp = le_assinatura()
textos = le_textos()

# Avaliação e comparaçao de assinaturas dos textos
print("\nO autor do texto %i está infectado com COH-PIAH" % (avalia_textos(textos,ass_cp)))
