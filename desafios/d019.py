import random
valor_aleatorio = random.randint(1, 5)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 5: '))
    if chute > valor_aleatorio:
        print('Chute foi maior que o valor gerado!')
    elif chute < valor_aleatorio:
        print('Chute foi menor que o valor gerado!')
    elif chute == valor_aleatorio:
        print('Você acertou!')
        acertou = True
    else:
        print('Chute um número de 1 a 5')