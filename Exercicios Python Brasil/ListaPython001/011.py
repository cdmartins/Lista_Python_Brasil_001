#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
#a produto do dobro do primeiro com metade do segundo .
#b soma do triplo do primeiro com o terceiro.
#cterceiro elevado ao cubo. 

n1 = float (input("Digite um numero inteiro: "))
n2 = float(input("Digite outro numero inteiro: "))
n3 = float(input("Digite um numero real: "))

a = (n1*2) + (n2 /2)
b = (n1*3) + n3
c = n3**3

print(f'{a}, {b}, {c}')
