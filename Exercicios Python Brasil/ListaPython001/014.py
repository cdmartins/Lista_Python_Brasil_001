pesoPeixe = float (input("Peso: "))
if pesoPeixe > 50: 
    excesso = pesoPeixe -50 
else: excesso = 0

multa = 0

if(pesoPeixe > 50):
    multa = multa +(4* excesso)

print(f'Você pagará R${multa} de multa pois excedeu {excesso}KG')
