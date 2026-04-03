#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
real = float(input('Quanto você tem na carteira? R$').replace(',','.'))
cotacao = float(input('Digite a cotação do dólar: ').replace(',','.'))
dolar = real / cotacao
print (f'Com valor que você tem na carteira, você pode comprar US${dolar:.2f} dolares.')
