# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Informe seu salário atual: '))
aumento = salario * 0.15
salario_atual = salario + aumento

print('Seu salário com o aumento é: {:.2f}'.format(salario_atual))