#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o seu salário atual? '))
novo = salario + (salario * 15 / 100)
print (f'Seu salário era de {salario:.2f} e seu novo salário com o aumento de 15% ficará {novo:.2f}')