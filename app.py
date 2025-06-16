import streamlit as st
import random
from gerador import gerar_matriz_de_jogos, gerar_jogos_simples
from api import obter_ultimos_concursos, obter_ultimo_resultado
from utils import salvar_em_txt, obter_top_dezenas

st.set_page_config(page_title="Mega-Sena Inteligente", layout="centered")
st.title("🔢 Gerador Inteligente de Jogos - Mega-Sena")

st.markdown("### 📌 Parâmetros do Jogo")
qtd_cartoes = st.number_input("Quantidade de cartões", min_value=1, max_value=500, value=10)
qtd_dezenas = st.number_input("Quantidade de dezenas por cartão", min_value=6, max_value=15, value=6)
usar_estrategia = st.checkbox("Usar estratégia com dezenas fixas (baseada em matriz)", value=True)

st.markdown("---")
if st.button("🎲 Gerar Jogos"):
    if usar_estrategia:
        concursos = obter_ultimos_concursos(qtd=20)
        dezenas_escolhidas = obter_top_dezenas(concursos, top_n=10)
        dezenas_fixas = dezenas_escolhidas[:4]
        jogos = gerar_matriz_de_jogos(dezenas_escolhidas, dezenas_fixas, qtd_cartoes)
        st.success(f"Jogos gerados com base estatística! Fixas: {dezenas_fixas}")
    else:
        jogos = gerar_jogos_simples(qtd_cartoes, qtd_dezenas)
        st.success("Jogos simples gerados com sucesso!")

    for i, jogo in enumerate(jogos, 1):
        st.write(f"Jogo {i}: {', '.join(f'{n:02}' for n in jogo)}")

    caminho = salvar_em_txt(jogos)
    with open(caminho, "rb") as file:
        st.download_button("⬇️ Baixar jogos em TXT", file, file_name="jogos_mega.txt")

st.markdown("---")
if st.button("🔍 Ver último resultado da Mega-Sena"):
    dezenas = obter_ultimo_resultado()
    st.info(f"Último resultado: {', '.join(str(d) for d in dezenas)}")

st.markdown("---")
st.caption("🔧 Desenvolvido por SAM ROCK • Todos os direitos reservados • 2025")