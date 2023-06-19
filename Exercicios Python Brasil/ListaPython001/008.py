#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês. 

valorPorHora = float (input('Valor por hora trabalhada: '))
horasTrabalhadas = float(input('Total de horas: '))
salario = valorPorHora * horasTrabalhadas
print(f'Trabalhando por {round(horasTrabalhadas)}H, você receberá um salário de R${salario:.2f}')