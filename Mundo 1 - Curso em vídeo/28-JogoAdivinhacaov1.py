import random
print('Pense em um número entre 0 e 5')
number = random.randint(0, 5)
print('Pensei')

numU = int(input('Adivinhe o número: '))

if numU == number:
    print('Você acertou, o número era {}'.format(number))
else:
    print('\033[1;30;41mVocê errou o número era {}\033[m'.format(number))
