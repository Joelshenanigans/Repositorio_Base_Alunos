# criar um arquivo nomes.txt

nomes = ['joão\n','maria\n', 'ana\n'] # criamos uma lista com nomes para ser
## inseridos no arquivo nomes.txt


with open('nomes.txt', 'w', encoding = 'utf-8') as arquivo: # estamos
  # criando o arquivo 
    arquivo.writelines(nomes) # estamos pedindo para escrever



















