# criar arquivos, recebendo informação do usuário

# Solicitação de entrada

nome = input('digite seu nome completo:')
email = input('digite seu email:')

# Criar arquivo
arquivo = open('pessoa.txt', 'a', encoding = 'utf-8') # estamos criando o arquivo e
# armazenando na variavel arquivo, o modo 'a' escreve sempre no final,
# enconding utf-8 é para utilizar o conjunto de caracteres que engloba
# a limgua portuguesa
arquivo.write(nome +'|'+ email + '\n')
# \n é para pular linha
arquivo.close()













