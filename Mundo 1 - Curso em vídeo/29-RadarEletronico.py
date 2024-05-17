vel = float(input('Qual é a velocidade atual do carro? '))

if (vel > 80):
    multa = (vel-80)*7
    print('você foi MULTADO!\nValor da multa é de R${:.2f}'.format(multa))

print('Tenha um bom dia! Dirija com seguraça!')
