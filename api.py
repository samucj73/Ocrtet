import requests

def obter_ultimo_resultado():
    url = 'https://api.guidi.dev.br/loteria/megasena/ultimo'
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    dezenas = dados.get('listaDezenas', [])
    return [int(d) for d in dezenas]