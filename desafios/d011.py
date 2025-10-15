# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Informe o preço do produto: '))
desconto = preco * 0.05
valor_final = preco - desconto

print('O produto ficou {:.2f}'.format(valor_final),'com o desconto.')