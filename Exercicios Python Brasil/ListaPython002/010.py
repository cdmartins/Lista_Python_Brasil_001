#Faça um Programa que pergunte em que turno você estuda. 
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = str (input('Qual turno voce estuda? [M] [V] [N]'))
if (turno == 'M'):
    print('Bom dia, aluno.')
elif (turno == 'V'):
    print('Boa tarde, aluno.')
elif (turno == 'N'):
    print('Boa noite, aluno')
else: print ('Turno Invalido')