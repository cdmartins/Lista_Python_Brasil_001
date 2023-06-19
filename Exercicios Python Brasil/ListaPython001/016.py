import math

area = float (input("Area em m²: "))
coberturaLitros = area / 3
lata = 0
if coberturaLitros > 18:
    lata = lata + (coberturaLitros / 18)
else: lata = 0
preco = math.ceil(lata) * 80
print(f'Você precisará de {math.ceil(lata)}: latas de tintas totalizando R${preco:.2f}')