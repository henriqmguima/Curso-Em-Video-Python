n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
n3 = int(input('3º valor: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        menor = n3
    else:
        menor = n2
    print('O maior número é {}\nO menor número é {}'.format(n1, menor))
elif n2 > n3:
    if n1 > n3:
        menor = n3
    else:
        menor = n1
    print('O maior número é {}\nO menor número é {}'.format(n2, menor))
else:
    if n2 > n1:
        menor = n1
    else:
        menor = n2
    print('O maior número é {}\nO menor número é {}'.format(n3, menor))
