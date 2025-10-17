# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome


nome = input('Digite seu nome completo: ')
print(nome.upper()) # maiúsculas
print(nome.lower()) # minúsculas
print((len(nome.replace(' ','')))) # quantidade de letras sem espaço

nome = nome.split() # dividindo string em coleções
print(len(nome[0])) # letras do primeiro nome

# Desafio concluído ;)