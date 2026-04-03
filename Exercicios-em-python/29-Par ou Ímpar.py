#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
from time import sleep
print('-=-' * 18)
n = int(input('Digite um número para saber se ele é par ou ímpar: '))
print ('PROCESSANDO...')
sleep(2)
if n % 2 == 0:
    print('O número digitado é \033[0;7;40mpar!\033[m')
else:
    print('O número digitado é \033[0;7;40mímpar!\033[m')
