# Desenvolva um programa que leia as notas de um aluno, calcule e mostre sua média

aluno = input('Digite o nome do aluno: ')
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('O aluno',aluno,'teve a média semestral:',media)

if(media >= 6) :
    print('O aluno',aluno,'está na média.')
else:
    print('O aluno',aluno,'está de recuperação.')