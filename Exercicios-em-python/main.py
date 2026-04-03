#Calculadora em python
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
operacao = (input('Digite a operação: '))

match operacao:
    case '+':
        res = (num1 + num2)
    case '-':
        res = (num1 - num2)
    case '*':
        res = (num1 * num2)
    case '/':
        res = (num1 / num2)

print (f'O resultado é igual a \033[4;30;107m{res}\033[m')

