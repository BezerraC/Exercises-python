# Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua area e a quantidade de tinta
# necessario para pinta-la, sabendo que cada litro de tinta pinda uma area de 2mˆ2.

a = float(input('Altura da parede em metros: '))
l = float(input('Largura da parede em metros: '))
ae = a*l
p = ae/a
print('Sua area é: {}m2 e você ira precisar de {} litros de tinta'.format(ae, p))
