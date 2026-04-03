#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
sin = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {sin:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tan:.2f}')

