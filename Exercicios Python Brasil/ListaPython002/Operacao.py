n1 = float(input('Primeiro Numero: '))
n2 = float(input('Segundo Numero: '))
operacao = input('Qual operacao deseja fazer entre eles? \n1 - [+] \n2 - [-] \n3 - [*] \n4 - [/] ')
if (operacao == '1'):
    resultado = n1 + n2
elif (operacao == '2'):
    resultado = n1 - n2
elif (operacao == '3'):
    resultado = n1 * n2
elif (operacao == '4'):
    resultado = n1 / n2

texto = 'DECIMAL' if round(resultado) != resultado else'INTEIRO'

print(f'\n{resultado}\n{texto}')

if (resultado %2 == 0): 
    print ('PAR')
else: print('IMPAR')
if (resultado > 0):
    print('POSITIVO')
elif (resultado == 0):
    print('0 é um numero NEUTRO')
else: print('É um numero NEGATIVO')

