sal = float(input('Qual é o salário do funcionário? R$'))

if sal > 1250:
    aum = ((sal*10)/100)+sal
else:
    aum = ((sal*15)/100)+sal
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, aum))
