# crie um programa que leia o peso de 5 pessoas
# no final, mostre qual foi o maior e o menor peso lido

# etapas para resultado:
# 1) crie uma lista vazia para receber os pesos
# 2) crie um for para receber os pesos das 5 pessoas
# 3) adicione os pesos recebidos a lista
# 4) utilize a função max() e min() 
# ou ordene a lista e busque o primeiro e o ultimo elemento
# 5) apresente os resultados


pesos = []

for i in range(5):
    peso = float(input(f'digite seu peso em kg: '))
    pesos.append(peso)
print(f'a lista dos pesos em kg: ')

#maior_peso = max(pesos)
#menor_peso = min(pesos)
#print(f'o maior peso é {maior_peso} kg e o menor peso é {menor_peso} kg')

# outra maneira de resolver o maior e o menor
pesos.sort()
menor = pesos[0]
maior = pesos[-1]
print(f'o maior peso é {maior} kg e o menor peso é {menor} kg')



