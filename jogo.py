import funcoes
inicio = input('Você deseja jogar? (s/n) ')
if inicio == 's':
    jogar = True
    print(funcoes.cria_baralho())
else:
    print('Não vai jogar')