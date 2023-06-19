ValorCarne = 0
desconto = 0
totalComDesconto = 0

TipoCarne = input("Qual o tipo de carne? * File Duplo / Alcatra / Picanha * ")
if (TipoCarne == 'Picanha'):    
    ValorCarne = 6.9    
elif (TipoCarne == 'Alcatra'):
        ValorCarne = 5.9        
else: ValorCarne = 4.9          

QtdCarne = float(input("Quantos kg? "))
if (QtdCarne > 5):
      ValorCarne +=1
totalSemDesconto = (QtdCarne * ValorCarne)

pagamento = input('Qual a forma de pagamento? ')
if (pagamento == 'Cartao da loja'):
      desconto = totalSemDesconto * 0.05
      totalComDesconto = totalSemDesconto * 0.95
          
              
print (f'Tipo de carne: {TipoCarne} \nQuantidade (kg): {QtdCarne:.2f} \nPreço total: {totalSemDesconto:.2f} \nTipo de Pagamento: {pagamento} \nValor do desconto: {desconto:.2f} \nValor a pagar: {totalSemDesconto:.2f}')