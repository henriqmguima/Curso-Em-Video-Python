preco = float(input('Qual é o preço do produto? R$'))
desc = (preco*5)/100
print(
    'O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar {:.2f}'.format(preco, preco-desc))
