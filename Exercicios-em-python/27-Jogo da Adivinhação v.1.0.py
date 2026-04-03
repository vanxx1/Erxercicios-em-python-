#Jogo de adivinhação v.1.0
import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
computador = random.randint(0,5)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...' )
sleep(2)
if jogador == computador:
    print('Parabéns você me venceu!' )
else:
    print(f'GANHEI! eu pensei no número {computador}. ')
