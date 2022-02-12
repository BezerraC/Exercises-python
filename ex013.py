# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salario, com 15% de aumento.

s = float(input('Digite seu salário: '))
c = (s*15)/100
ns = s + c
print('Seu salario passou de R${} para R${} com 15% de aumento'.format(s, ns))
Ec