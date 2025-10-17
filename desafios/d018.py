# faça um programa que leia o nome completo de uma pessoa, mosrando em seguida o primeiro e o último nome separadamente.

# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = input('Digite seu nome completo: ')
nome = nome.split()

print('primeiro nome:',nome[0])
print('último nome:',nome[-1]) # mostra a última string

