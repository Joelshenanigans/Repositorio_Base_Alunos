# 








notas = []

for i in range(4):
    nota = float(input(f'informe a nota da prova {i+1}: '))
    if nota > 0:
        notas.append(nota)
    else:
        print('valor invalido')
print(f'suas notas são: {notas}') # linha opcional
media = sum(notas)/len(notas)

if media >= 7:
   print(f'suas notas foram {notas}, sua {media:.2f} e você está aprovado')
elif 5 <= media < 7:
   print(f'suas notas foram {notas}, sua {media:.2f} e você está de recuperação')
else:
   print(f'suas notas foram {notas}, sua {media:.2f} e você está repovado')








