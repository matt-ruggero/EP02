def cria_baralho():
    import random
    baralho =[]
    for i in range(0, 13):
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        naipes = ['♠', '♦', '♣', '♥']
        carta_e = valores[i] + naipes[0]
        carta_o = valores[i] + naipes[1]
        carta_p = valores[i] + naipes[2]
        carta_c = valores[i] + naipes[3]
        baralho.append(carta_e)
        baralho.append(carta_o)
        baralho.append(carta_p)
        baralho.append(carta_c)
        random.shuffle(baralho)
    return baralho

def extrai_naipe(x):
    if '♦' in x:
        return '♦'
    if '♥' in x:
        return '♥'
    if '♣' in x:
        return '♣'
    if '♠' in x:
        return '♠'

def extrai_valor(x):
    if 'A' in x:
        return 'A'
    if '2' in x:
        return '2'
    if '3' in x:
        return '3'
    if '4' in x:
        return '4'
    if '5' in x:
        return '5'
    if '6' in x:
        return '6'
    if '7' in x:
        return '7'
    if '8' in x:
        return '8'
    if '9' in x:
        return '9'
    if '10' in x:
        return '10'
    if 'J' in x:
        return 'J'
    if 'Q' in x:
        return 'Q'
    if 'K' in x:
        return 'K'

def lista_movimentos_possiveis(baralho, i):
    movimentos = []
    if i == 0:
        return []
    if '♥' in baralho[i] and '♥' in baralho[i-1]:
        movimentos.append(1)
    if '♣' in baralho[i] and '♣' in baralho[i-1]:
        movimentos.append(1)
    if '♠' in baralho[i] and '♠' in baralho[i-1]:
        movimentos.append(1)
    if '♦' in baralho[i] and '♦' in baralho[i-1]:
        movimentos.append(1)
    if 'A' in baralho[i] and 'A' in baralho[i-1]:
        movimentos.append(1)
    if '2' in baralho[i] and '2' in baralho[i-1]:
        movimentos.append(1)
    if '3' in baralho[i] and '3' in baralho[i-1]:
        movimentos.append(1)
    if '4' in baralho[i] and '4' in baralho[i-1]:
        movimentos.append(1)
    if '5' in baralho[i] and '5' in baralho[i-1]:
        movimentos.append(1)
    if '6' in baralho[i] and '6' in baralho[i-1]:
        movimentos.append(1)
    if '7' in baralho[i] and '7' in baralho[i-1]:
        movimentos.append(1)
    if '8' in baralho[i] and '8' in baralho[i-1]:
        movimentos.append(1)
    if '9' in baralho[i] and '9' in baralho[i-1]:
        movimentos.append(1)
    if '10' in baralho[i] and '10' in baralho[i-1]:
        movimentos.append(1)
    if 'J' in baralho[i] and 'J' in baralho[i-1]:
        movimentos.append(1)
    if 'Q' in baralho[i] and 'Q' in baralho[i-1]:
        movimentos.append(1)
    if 'K' in baralho[i] and 'K' in baralho[i-1]:
        movimentos.append(1)
    if i >= 3:
        if '♥' in baralho[i] and '♥' in baralho[i-3]:
            movimentos.append(3)
        if '♣' in baralho[i] and '♣' in baralho[i-3]:
            movimentos.append(3)
        if '♠' in baralho[i] and '♠' in baralho[i-3]:
            movimentos.append(3)
        if '♦' in baralho[i] and '♦' in baralho[i-3]:
            movimentos.append(3)
        if 'A' in baralho[i] and 'A' in baralho[i-3]:
            movimentos.append(3)
        if '2' in baralho[i] and '2' in baralho[i-3]:
            movimentos.append(3)
        if '3' in baralho[i] and '3' in baralho[i-3]:
            movimentos.append(3)
        if '4' in baralho[i] and '4' in baralho[i-3]:
            movimentos.append(3)
        if '5' in baralho[i] and '5' in baralho[i-3]:
            movimentos.append(3)
        if '6' in baralho[i] and '6' in baralho[i-3]:
            movimentos.append(3)
        if '7' in baralho[i] and '7' in baralho[i-3]:
            movimentos.append(3)
        if '8' in baralho[i] and '8' in baralho[i-3]:
            movimentos.append(3)
        if '9' in baralho[i] and '9' in baralho[i-3]:
            movimentos.append(3)
        if '10' in baralho[i] and '10' in baralho[i-3]:
            movimentos.append(3)
        if 'J' in baralho[i] and 'J' in baralho[i-3]:
            movimentos.append(3)
        if 'Q' in baralho[i] and 'Q' in baralho[i-3]:
            movimentos.append(3)
        if 'K' in baralho[i] and 'K' in baralho[i-3]:
            movimentos.append(3)
    return movimentos

def empilha(baralho, i, i_n):
    baralho[i_n] = baralho[i]
    del(baralho[i])
    return baralho

def possui_movimentos_possiveis(movimentos):
    if movimentos != []:
        return True
    else:
        return False

def fim_do_jogo(baralho):
    movimentos_possiveis = []
    for i in range(1, len(baralho)):
        movimentos = lista_movimentos_possiveis(baralho, i)
        if len(movimentos) > 0:
            movimentos_possiveis.append(1)
    if movimentos_possiveis == []:
        return True
    else:
        return False

def cartas_em_lista(baralho):
    lista_cartas = ''
    w = 0
    for i in range(1, len(baralho)+1):
        lista_cartas += ('{0}. {1}\n'.format(i, baralho[w]))
        w += 1
    return lista_cartas