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
    i = int(input('Escolha uma carta: ')) - 1
    movimentos = funcoes.lista_movimentos_possiveis(baralho, i)
    poder = funcoes.possui_movimentos_possiveis(movimentos)