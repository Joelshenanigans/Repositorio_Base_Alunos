# crie uma api que consulte o cep e informe o endereço

# Iniciamos fazendo a importação da biblioteca requests
import requests 

# indicamos a url para consulta da api
cep = input('Digite o CEP (somente números): ').strip() # usuario informa o cep que deseja consultar
url = f'https://viacep.com.br/ws/{cep}/json' # endereço de url formatado para requests do cep

# fazemos a requisição
resposta = requests.get(url) # aqui estamos fazendo a requisição

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' not in dados:
        print(f'CEP: {dados['cep']}')
        print(f'Logradouro: {dados['bairro']}')
        print(f'Bairro: {dados['bairro']}')
        print(f'Cidade: {dados['Localidade']}')
        print(f'Estado: {dados['uf']}')
    else:
        print('CEP não foi encontrado')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)







