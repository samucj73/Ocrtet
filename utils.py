def salvar_em_txt(jogos, nome_arquivo="jogos_mega.txt"):
    with open(nome_arquivo, "w") as f:
        for idx, jogo in enumerate(jogos, 1):
            f.write(f"Jogo {idx}: {', '.join(f'{n:02}' for n in jogo)}\n")
    return nome_arquivo