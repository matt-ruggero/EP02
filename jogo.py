import funcoes
inicio = input('Você deseja jogar? (s/n) ')
if inicio == 's':
    jogar = True
    baralho = funcoes.cria_baralho()
    print(baralho)
else:
    print('Não vai jogar')
    jogar = False