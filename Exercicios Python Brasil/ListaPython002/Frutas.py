morango = float(input('Peso do MORANGO(kg): '))
pesoDoMorango = morango 
if (pesoDoMorango <= 5):
    p1 = morango * 2.5
else: p1 = morango * 2.2

maca = float(input('Peso da MAÇÃ(kg): '))
pesoDaMaca = maca
if (pesoDaMaca <= 5):
    p2 = maca * 1.8
else:  p2  = maca * 1.5
precoTotal = p1 + p2
desconto = 0
if ((pesoDoMorango + pesoDaMaca) >= 8) or (precoTotal >= 25):
    precoTotal = precoTotal * 0.90
    desconto = precoTotal * 0.10
else: precoTotal = p1 + p2
totalApagar = precoTotal - desconto

print(f'Você adquiriu {pesoDoMorango}kg de Morango e {pesoDaMaca}kg de Maça \n >> Totalizando R${precoTotal:.2f} \n >> Desconto de R${desconto:.2f} \n >> Total a pagar: R${totalApagar:.2f}')




