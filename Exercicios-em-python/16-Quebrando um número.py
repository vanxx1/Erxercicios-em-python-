#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: Digite um número:6.127
#O número 6.127 tem a parte inteira 6.
from math import trunc
num = float(input('Digite um número para saber sua parte inteira: '))
parte_inteira = trunc(num)
print(f'A parte inteira do número {num} é igual a {parte_inteira}')

