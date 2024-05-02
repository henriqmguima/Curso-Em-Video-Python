import random
al1 = input('nome do 1º aluno: ')
al2 = input('nome do 2º aluno: ')
al3 = input('nome do 3º aluno: ')
al4 = input('nome do 4º aluno: ')

lista = [al1, al2, al3, al4]
print('O aluno escolhido foi {}'.format(random.choice(lista)))
