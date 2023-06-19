ano = (input('Ano: '))
if (len(ano) == 4):
    if (int(ano) % 4 == 0):
        print(ano, ' é um ano BISSEXTO')
    else:
        print(ano, ' não é um ano BISSEXTO')
else:
    print('Ano invalido, favor digitar 4 digitos.')
