#Faça um Programa que leia três números e mostre-os em ordem decrescente. 

lista = []

for n in range(3):
    n = int (input(f'Digite {n+1}º numero: '))
    lista.append(n)

print()
lista.sort(reverse=True)
print(lista)
