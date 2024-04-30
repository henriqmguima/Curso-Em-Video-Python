sal = float(input('Qual é o salário do funcionário? R$'))
aum = (sal*15)/100
print('Um funcionário que ganhava R${:.2f}, com aumento de 15% de aumento, passa a receber R${:.2f}'.format(
    sal, sal+aum))
