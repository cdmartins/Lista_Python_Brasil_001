Total= 0
p1 = input('Telefonou para a vítima? ')
print (p1)
Total += 1 if p1 == 'Sim' else 0    
p2 = input('Esteve no local do crime? ')
print (p2)
Total += 1 if p2 == 'Sim' else 0
p3 = input('Mora perto da vítima? ')
print (p3)
Total += 1 if p3 == 'Sim' else 0
p4 = input('Devia para a vítima? ')
print (p4)
Total += 1 if p4 == 'Sim' else 0
p5 = input('Já trabalhou com a vítima? ')
print (p5)
Total += 1 if p5 == 'Sim' else 0
if (Total == 2):
     print('Suspeito')
elif (Total >= 3 and Total <= 4):
    print('Cumplice')
elif(Total == 5):
    print('Assassino')
else: print('Inocente')