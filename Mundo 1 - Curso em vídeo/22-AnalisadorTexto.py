nome = input('Digite seu nome completo: ')

print('Seu nome em letras maiúsculas é '.format(nome.upper()))
print('Seu nome me letras minúsculas é '.format(nome.lower()))

print('Seu nome completo tem {} letras'.format(len(nome.replace(" ", ""))))

firsName = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(firsName[0])))
