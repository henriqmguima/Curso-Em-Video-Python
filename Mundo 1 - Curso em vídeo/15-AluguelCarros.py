dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preco = (km*0.15)+(dias*60)
print('O total a pagar é de R${:.2f}'.format(preco))
