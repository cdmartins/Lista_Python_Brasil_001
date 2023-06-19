TipoCarne = input("Qual o tipo de carne? ")
if (TipoCarne == 'Picanha'):
    ValorCarne = 6.9
elif (TipoCarne == 'Alcatra'):
    ValorCarne = 5.9
else:
    ValorCarne = 4.9

QtdCarne = float(input("Quantos kg? "))
if (QtdCarne > 5):
    ValorCarne = ValorCarne + 0.90

preco_carne1 = (QtdCarne * ValorCarne)

pagamento = input('Qual a forma de pagamento? ')
if (pagamento == 'Cartao da loja'):
    desconto = preco_carne1 * 0.05
    preco_carne = preco_carne1 - desconto
else: preco_carne = preco_carne1


print(f'Tipo de carne: {TipoCarne} \nQuantidade (kg): {QtdCarne} \nPreço total: {preco_carne1:.2f} \nTipo de Pagamento: {pagamento} \nValor do desconto: {desconto:.2f} \nValor a pagar: {preco_carne:.2f}')
