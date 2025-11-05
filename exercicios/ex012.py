n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('Sua média é {}.'.format(m))
print('Parabéns. Você está na média' if m >= 6 else 'Que pena. Você está de recuperação.')