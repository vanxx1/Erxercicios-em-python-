#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas minusculas
#Quantas letras ao total(sem considerar espaços).
#Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

#Nome em letras maiúsculas
print(f'Seu nome em maiúsculas: {nome.upper()}')

#Nome em letras minusculas
print(f'Seu nome em minúsculas: {nome.lower()}')

#Letras ao total sem espaços
nome = nome.replace('  ',' ')
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras')

#Letras do primeiro nome
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras')
