#Faça um Programa que peça a temperatura em graus Fahrenheit
#transforme e mostre a temperatura em graus Celsius. 
#C = 5 * ((F-32) / 9). 

tempF = float (input("Digite a temperatura em graus Fahrenheit: "))
tempCel = 5*((tempF-32)/9)
print(f'{tempF}°F equivale a {tempCel:.1f}°C')