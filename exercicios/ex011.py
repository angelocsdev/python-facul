# Condições

# simples -> só tem o if
# composta -> if e else

nome = str(input('Qual é o seu nome? '))
# if nome == "Gabriel":
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é bonitinho!')
print('Que nome lindo você tem!' if nome == "Gabriel" else 'Seu nome é bonitinho!') # condição simplificada
print('Bom dia, {}!'.format(nome))
