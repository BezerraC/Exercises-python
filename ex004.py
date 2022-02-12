# crie um programa que leia algo pelos tecaldo e mostre na tela o
# seu tipo primitivo e todas as informações possíveis sobre ele

algo = input('Digite algo: ')
print('O tipo primitivo dessa valor é: {} '.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está em maiúscula? {}'.format(algo.isupper()))
print('Ésta em minúscula? {}'.format(algo.islower()))
print('Ésta capitalizada? {}'.format(algo.istitle()))

