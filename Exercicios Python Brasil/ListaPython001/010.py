#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 

grausCel = float (input("Digite a temperatura em graus Celsius: "))
grausFah = ((grausCel * 1.8)+32)
print(f'{grausCel}°C equivale a {grausFah:.1f}°F')