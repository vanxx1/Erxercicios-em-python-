#Radar eletrônico
#escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$7,0 para cada km acima do limite
v = int(input('Qual a velocidade atual do carro? '))
if v > 80:
    print(f'Você deve pagar uma multa de R${(v - 80) * 7}')
else:
    print('Tenha um bom dia! Dirija com segurança!')
