import requests

def obter_ultimo_resultado():
    url = 'https://api.guidi.dev.br/loteria/megasena/ultimo'
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    dezenas = dados.get('listaDezenas', [])
    return [int(d) for d in dezenas]

def obter_ultimos_concursos(qtd=20):
    url = f'https://api.guidi.dev.br/loteria/megasena/{qtd}'
    response = requests.get(url)
    response.raise_for_status()
    concursos = response.json()  # corrigido: agora trata como lista direta
    resultados = []
    for c in concursos:
        dezenas = c.get('listaDezenas', [])
        numeros = [int(d) for d in dezenas]
        resultados.append(numeros)
    return resultados