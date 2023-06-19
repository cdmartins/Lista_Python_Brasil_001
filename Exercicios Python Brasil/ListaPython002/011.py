salario_atual = float (input('Salário Atual: '))
if (salario_atual <= 280):
    reajuste = salario_atual*0.20
    aumento = '20%'
elif (salario_atual > 280 and salario_atual <= 700):
    reajuste = salario_atual*0.15
    aumento = '15%'
elif (salario_atual > 700 and salario_atual <= 1500):
    reajuste = salario_atual*0.10
    aumento = '10%'
elif salario_atual > 1500:
    reajuste = salario_atual*0.05 
    aumento = '5%'

novo_salario = salario_atual + reajuste

print(f' Salário atual: R${salario_atual} \n Porcentual de aumento: R${aumento} \n Valor do reajuste: R${reajuste} \n Novo Salario: R${novo_salario}')