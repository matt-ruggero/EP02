import funcoes
inicio = input('Você deseja jogar? (s/n) ')
if inicio == 's':
    jogar = True
    baralho = funcoes.cria_baralho()
    print(baralho)
else:
    print('Não vai jogar')
    jogar = False

while jogar:
    final = funcoes.fim_do_jogo(baralho)
    if final:
        if baralho == []:
            print('Alguma coisa deu errado')
            jogar = False
        elif len(baralho) == 1:
            print('Parabéns você ganhou!')
            jogar = False
            break
        else:
            print('Você perdeu, melhor sorte na próxima.')
            jogar = False
            break
    i = int(input('Escolha uma carta: '))
    movimentos = funcoes.lista_movimentos_possiveis(baralho, i)
    poder = funcoes.possui_movimentos_possiveis(movimentos)
    if poder:
        if 1 in movimentos and 3 in movimentos:
            print('1.{0}'.format(baralho[i-1]))
            print('2.{0}'.format(baralho[i-3]))
            carta_escolhida = int(input('Sobre qual carta você quer empilhar o {0}?'.format(baralho[i])))
            if carta_escolhida == 1:
                i_novo = i-1
                baralho = funcoes.empilha(baralho, i, i_novo)
                print(baralho)
                poder = False
            else:
                i_novo = i-3
                baralho = funcoes.empilha(baralho, i, i_novo)
                print(baralho)
                poder = False
        elif 1 in movimentos:
            i_novo = i-1
            baralho = funcoes.empilha(baralho, i, i_novo)
            print(baralho)
            poder = False
        elif 3 in movimentos:
            i_novo = i-3
            baralho = funcoes.empilha(baralho, i, i_novo)
            print(baralho)
            poder = False
    else:
        print('Essa não dá')