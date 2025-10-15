# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('é um número? ', a.isnumeric())
print('É alfabético? ',a.isalpha())
print('é alfanumérico? ',a.isalnum())
print('maiusculo: ',a.isupper())
print('minusculo: ',a.islower())
print('Está capitalizada?',a.istitle())