import math
area = float (input("Area em m²: "))
coberturaLitros = area / 6
lata = 0
if coberturaLitros > 18:
    lata = lata + (coberturaLitros / 18)
else: lata = 0
galao = 0
if coberturaLitros > 3.6:
    galao = galao +(coberturaLitros / 3.6)
else: galao = 0

precoGalao= math.ceil(galao) * 25
precoLata = math.ceil(lata) * 80

print(f'preco em lata {precoLata} preco em galao {precoGalao}')

#incompleto