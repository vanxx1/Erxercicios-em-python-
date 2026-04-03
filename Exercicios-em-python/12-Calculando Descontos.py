#Faça um algoritmo que leia preço de um produto e mostre seu novo preço, com 5% de desconto.
#Ler preço do produto
preco = float(input('Digite o valor do produto : R$ '))

#Calculando desconto de 5%
desconto = preco * 0.05
novo_preco = preco - desconto

print(f'O produto que custava \033[32mR${preco}\033[m com desconto de 5% fica \033[33mR${novo_preco}\033[m')


