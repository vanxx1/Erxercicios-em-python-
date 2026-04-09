#Faça um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = float(input('Digite um valor:'))
print (f'O valor de metros digitado em Quilômetro é {m / 1000}km')
print (f'O valor de metros digitado em Hectômetro é {m / 100}hm')
print (f'O valor de metros digitado em Decâmetro é {m / 10}dam')
print (f'O valor de metros digitado em Decímetro é {m * 10:.0f}dm')
print (f'O valor de metros digitado em Centimetro é {m * 100:.0f}cm')
print (f'O valor de metros digitado em Milímetro é {m * 1000:.0f}mm')

