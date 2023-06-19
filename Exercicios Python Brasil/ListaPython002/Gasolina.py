alcool = 1.9
gasolina = 2.5

combustivel = (input('Combustivel: [A] - álcool [G] - Gasolina '))
if (combustivel == 'G'):
    preco = 2.5
elif (combustivel == 'A'):
    preco = 1.9
else:
    print('Combustivel Inválido')

litros = float(input('Quantos litros? '))
porLitro = preco * litros
print(f'Valor sem desconto: R${porLitro:.2f}')

# GASOLINA
if ((combustivel == 'G') and (litros <= 20)):
    valorTotal = porLitro - ((gasolina * 0.04) * litros)
elif ((combustivel == 'G') and (litros > 20)):
    valorTotal = porLitro - ((gasolina * 0.06) * litros)
# ALCOOL
if ((combustivel == 'A') and (litros <= 20)):
    valorTotal = porLitro - ((alcool * 0.03) * litros)
elif ((combustivel == 'A') and (litros > 20)):
    valorTotal = porLitro - ((alcool * 0.05) * litros)

print(f'O valor a pagar com desconto: R${valorTotal:.2f}')

