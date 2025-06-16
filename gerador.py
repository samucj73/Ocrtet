import itertools
import random

def gerar_matriz_de_jogos(dezenas_totais, dezenas_fixas, qtd_jogos=7):
    dezenas_variaveis = list(set(dezenas_totais) - set(dezenas_fixas))
    combinacoes = list(itertools.combinations(dezenas_variaveis, 2))
    random.shuffle(combinacoes)

    jogos = []
    for comb in combinacoes[:qtd_jogos]:
        jogo = sorted(dezenas_fixas + list(comb))
        jogos.append(jogo)
    return jogos

def gerar_jogos_simples(qtd_cartoes, qtd_dezenas):
    todos_numeros = list(range(1, 61))
    jogos = []
    for _ in range(qtd_cartoes):
        jogo = sorted(random.sample(todos_numeros, qtd_dezenas))
        jogos.append(jogo)
    return jogos