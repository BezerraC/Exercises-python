# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# Considerando o Dolar a R$ 3,27

d = float(input('Informe sua quantia em dinheiro: '))
c = d/3.27
print('Com R$ {} você pode comprar $ {:.2f} Dólares'.format(d, c))
