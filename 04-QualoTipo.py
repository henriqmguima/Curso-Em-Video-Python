coisa = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(coisa))
print('Só tem espaços? ', coisa.isspace())
print('É um númerico? ', coisa.isnumeric())
print('É um alfanúmerico? ', coisa.isalnum())
print('Está em maiúsculas? ', coisa.isupper())
print('Está em minúsculas? ', coisa.islower())
print('Está capitalizada? ', coisa.capitalize())
