# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

wallet = float(input('Quanto você tem para converter? '))
conversao = wallet / 5.45

print('Com esse dinheiro:',wallet,'.\nVocê pode comprar',conversao,'em dólares.')