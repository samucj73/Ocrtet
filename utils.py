from collections import Counter

def salvar_em_txt(jogos, nome_arquivo="jogos_mega.txt"):
    with open(nome_arquivo, "w") as f:
        for idx, jogo in enumerate(jogos, 1):
            f.write(f"Jogo {idx}: {', '.join(f'{n:02}' for n in jogo)}\n")
    return nome_arquivo

def obter_top_dezenas(concursos, top_n=10):
    todas = [dezena for concurso in concursos for dezena in concurso]
    contagem = Counter(todas)
    dezenas_mais_frequentes = [item[0] for item in contagem.most_common(top_n)]
    return sorted(dezenas_mais_frequentes)