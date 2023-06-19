#Faça um Programa que peça dois números e imprima o maior deles. 
n1 = int (input('Primeiro numero: '))
n2 = int (input('Segundo numero: '))

maior = f'O maior numero é {n1}' if n1 > n2 else f'O maior numero é {n2}'
print(maior)