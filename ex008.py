# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = float(input('Informe um valor em metros: '))
cm = m*100
mm = m*1000
print('{} metro(s) é igual a {} centimetros igual a {} milimetros'.format(m, cm, mm))
