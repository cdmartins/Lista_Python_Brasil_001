valorPorHora = float (input('Valor da hora trabalhada: '))
horasTrabalhadas = float(input('Total de horas: '))
salarioBruto = valorPorHora * horasTrabalhadas
IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = IR + INSS + sindicato
salarioLiquido = salarioBruto - descontos


print(f'+ Salário bruto R${salarioBruto:.2f} \n-IR = R${IR} \n-INSS = R${INSS:.2f} \n-Sindicato = R${sindicato:.2f} \nSalário Líquido = R${salarioLiquido}')