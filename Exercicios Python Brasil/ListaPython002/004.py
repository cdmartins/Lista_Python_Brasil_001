#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
letra = str (input('Letra: '))
letra = 'Vogal' if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u') else 'Consoante'
print(letra)