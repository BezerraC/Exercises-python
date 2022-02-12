# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input('Informe o valor do produto: '))
vd = (p*5)/100
d = p - vd
print('O preço era R$ {} agora com 5% de desconto ficou R$ {:.2f}'.format(p, d))

