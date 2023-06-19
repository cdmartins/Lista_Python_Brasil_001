#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
#Dica: utilize uma função de arredondamento. 
n1 = float(input('Digite um numero: '))
texto = 'DECIMAL' if round(n1) != n1 else'INTEIRO'
print(texto)