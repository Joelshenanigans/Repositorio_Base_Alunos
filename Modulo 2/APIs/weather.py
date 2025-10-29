# criar um codigo que consuma uma api de clima informe
# a trmperatura e a descrição de clima em um lugar especifico

# etapa
# 1. Definir chave de API e o link da requisição
import requests

api_key ='2a1ac38a32354cb7b19133643251408' # chave da api
cidade = input('Digite o nome da cidade: ').strip() # input para receber a informação do usuário e a função
url = f'https://api.weatherapi.com/v1/current.json' # url da api

# 2. Paramêtros da requisão
parametros ={
    'key':api_key,
    'q': cidade,
    'lang':'pt' # define a lingua da resposta como portugues
}

# 3. Fazer a requisição
resposta = requests.get(url, params=parametros)
# utilizamos o metodo get e informamos os parametros dessa requisição   

# 4. Verificar se a requisição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json() # converte a resposta json em  um dicionario python
    temperatura = dados['current']['temp_c']
    descrição = dados['current']['condition']['text']
    print(f'Temperatura na cidade {cidade} é {temperatura} °C')
    print(f'Descrição: {descrição}')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)







