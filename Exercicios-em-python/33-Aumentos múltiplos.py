#Escreva um programa que pergunte o sálario de um funcionário e
#calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)

else:
    aumento = salario + (salario * 10 / 100)

print(f'Quem ganhava \033[33mR${salario:.0f}\033[m passa a ganhar \033[32mR${aumento:.0f}\033[m agora!')
