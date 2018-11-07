# coding: utf-8

print('-=-' * 20)
print('Bem-vindo ao jogo do NIM!'.center(60, '='))
print('-=-' * 20)


def computador_escolhe_jogada(n, m):
    computador_tira = 1

    while computador_tira != m:
        if (n - computador_tira) % (m+1) == 0:
            return computador_tira

        else:
            computador_tira += 1

    return computador_tira


def usuario_escolhe_jogada(n, m):
    jogada_valida = False

    while not jogada_valida:
        jogador_tira = int(input('Quantas peças você vai tirar? '))
        if jogador_tira > m or jogador_tira < 1:
            print()
            print('\n:/ Oops! Jogada inválida! Tente de novo...')
            print()

        else:
        	jogada_valida = True

    return jogador_tira


def campeonato():
    numero_rodada = 1
    while numero_rodada <= 3:
        print()
        print('::::: Rodada', numero_rodada, ':::::')
        print()
        partida()
        numero_rodada += 1
    print()
    print('-> Placar: Você 0 X 3 Computador')


def partida():
    n = int(input('\nQuantas peças? '))

    m = int(input('\nLimite de peças por jogada? '))

    vez_pc = False

    if n % (m+1) == 0:
        print()
        print('\n -> Voce começa!')

    else:
        print()
        print('\n -> Computador começa!')
        vez_pc = True

    while n > 0:
        if vez_pc:
            computador_tira= computador_escolhe_jogada(n, m)
            n = n - computador_tira
            if computador_tira == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', computador_tira, 'peças')

            vez_pc = False
        else:
            jogador_tira = usuario_escolhe_jogada(n, m)
            n = n - jogador_tira
            if jogador_tira == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogador_tira, 'peças')
            vez_pc = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('\n\n :/  Fim do jogo! O computador ganhou!')


print('>>> Escolha:')
print()

print('1 - para jogar uma partida isolada')

partida_tipo = int(input('2 - para jogar um campeonato '))

if partida_tipo == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if partida_tipo == 1:
        print()
        partida()
