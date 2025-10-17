# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

cidade = input('Qual o nome da sua cidade? ')
cidade = cidade.split()
print('SANTO' in cidade[0])