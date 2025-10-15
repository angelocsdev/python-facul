'''
# adição
5 + 2
# subtração
5 - 2
# multiplicação
5 * 2
# divisão
5 / 2
# exponenciação
5 ** 2
# divisão inteira
5 // 2
# módulo / resto da divisão
5 % 2
'''

# Ordem de precedência

'''

1 -> (), parênteses
2 -> **, potência
3 -> * / // %
4 -> + -

'''

print(5 + 3 * 2) # 11
print(3 * 5 + 4 ** 2) # 31
print(3 * (5 + 4) ** 2) # 243

# Raízes quadradas e cúbicas

print(81 ** (1/2)) # O 1/2 multiplica o 81 por 0.5 que dá 9 que é a raiz quadrada

print(127 ** (1/3)) # mesma coisa só que pra raiz cúbica

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('soma {}, subtração{}, multiplicação {}, divisão {:.3f}'.format(s,sb,m,d), end=' ')
print('div inteira {}, exponenciação {}'.format(di,e))