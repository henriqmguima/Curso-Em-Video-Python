import math
op = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))

hip = math.hypot(op, ad)
print('A hipotenusa vai medir {:.2f}'.format(hip))
