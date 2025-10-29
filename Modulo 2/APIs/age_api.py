import requests 

# definir o nome para consulta

nome = input('Digite o nome da pessoa: ').strip()

# url da api
url = f'https://api.agify.io/?name={nome}'

# fazer a requisição
response = requests.get(url)

# Processar a resposta
if response.status_code == 200:
  dados = response.json()
  print(f'Nome:{dados['age']} anos')
  print(f'Idade estimada: {dados['age']} anos')
  print(f'Número de registros analisando: {dados['count']}')
else: 
  print(f'Erro ao acessar a API:{response.status_code}')







