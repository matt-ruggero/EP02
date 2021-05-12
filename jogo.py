import funcoes
inicio = input('Você deseja jogar? (s/n) ')
if inicio == 's':
    jogar = True
    baralho = funcoes.cria_baralho()
    print(funcoes.cartas_em_lista(baralho))
else:
    print('Não vai jogar')
    jogar = False

while jogar:
    final = False
    while not final:
        final = funcoes.fim_do_jogo(baralho)
        i = int(input('Escolha uma carta: ')) - 1
        if i >= len(baralho):
            print('Essa carta está fora dos limites do baralho atual')
        else:
            movimentos = funcoes.lista_movimentos_possiveis(baralho, i)
            poder = funcoes.possui_movimentos_possiveis(movimentos)
            if poder:
                if 1 in movimentos and 3 in movimentos:
                    print('1.{0}'.format(funcoes.cores(baralho[i-1])))
                    print('2.{0}'.format(funcoes.cores(baralho[i-3])))
                    carta_escolhida = int(input('Sobre qual carta você quer empilhar o {0}?'.format(funcoes.cores(baralho[i]))))
                    if carta_escolhida == 1:
                        i_novo = i-1
                        baralho = funcoes.empilha(baralho, i, i_novo)
                        print(funcoes.cartas_em_lista(baralho))
                        poder = False
                        final = funcoes.fim_do_jogo(baralho)
                    else:
                        i_novo = i-3
                        baralho = funcoes.empilha(baralho, i, i_novo)
                        print(funcoes.cartas_em_lista(baralho))
                        poder = False
                        final = funcoes.fim_do_jogo(baralho)
                elif 1 in movimentos:
                    i_novo = i-1
                    baralho = funcoes.empilha(baralho, i, i_novo)
                    print(funcoes.cartas_em_lista(baralho))
                    poder = False
                    final = funcoes.fim_do_jogo(baralho)
                elif 3 in movimentos:
                    i_novo = i-3
                    baralho = funcoes.empilha(baralho, i, i_novo)
                    print(funcoes.cartas_em_lista(baralho))
                    poder = False
                    final = funcoes.fim_do_jogo(baralho)
            else:
                print('Essa não dá')
                final = funcoes.fim_do_jogo(baralho)
    if baralho == []:
            print('Alguma coisa deu errado')
            jogar = False
    elif len(baralho) == 1:
            print('Parabéns você ganhou!')
            jogar_de_novo = input('Você deseja jogar de novo? (s/n): ')
            if jogar_de_novo == 's':
                jogar = True
                baralho = funcoes.cria_baralho()
                print(funcoes.cartas_em_lista(baralho))
            else:
                jogar = False
    else:
            print('Você perdeu, melhor sorte na próxima.')
            jogar_de_novo = input('Você deseja jogar de novo? (s/n): ')
            if jogar_de_novo == 's':
                jogar = True
                baralho = funcoes.cria_baralho()
                print(funcoes.cartas_em_lista(baralho))
            else:
                jogar = False