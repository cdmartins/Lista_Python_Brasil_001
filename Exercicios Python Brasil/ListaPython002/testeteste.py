h = float(input('Qual sua altura? '))
genero = input('Feminino [F]   /  Masculino [M] ')
if genero == 'F':
    peso_ideal = (62.1*h) - 44.7
else:
    peso_ideal = (72.7*h) - 58
print(
    f'O seu peso ideal é de {peso_ideal:.1f}Kg')
