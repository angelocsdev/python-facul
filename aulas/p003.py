frase = 'Curso em Vídeo Python'
print(frase[9:21:2]) # range -> o último valor não entra na contagem
# o 9 é o primeiro caractere exibido, o 21 o último - 1 e o 2 é os pulos de caracteres, nesse exemplo mostra de 2 em 2
print(frase[9::3]) # do 9 até o final porque não foi especificado o fim e pula de 3 em 3
print(len(frase)) # quantidade de caracteres da variável
print(frase.count('o',0,14)) # conta quantas letras tem
print(frase.find('Python')) # mostra onde começou
print('Curso' in frase) # existe curso in / em frase?
print(frase.replace('Python','Android')) # muda um conjunto de caracteres por outro, replace é trocar / reposicionar
print(frase.upper()) # deixa tudo maiusculo
print(frase.lower()) # deixa tudo em minusculo
print(frase.capitalize()) # deixa apenas a primeira letra da frase maiuscula
print(frase.title()) # todos os inicios de frase ficam maiusculos
print(frase.strip()) # tira os espaços sobrando do inicio e do final
print(frase.rstrip()) # remoce somente os últimos espaços
print(frase.lstrip()) # remoce somente os primeiros espaços
print(frase.split()) # separa a string pelos espaços -> ['Curso', 'em', 'Vídeo', 'Python']
print('-'.join(frase)) # preenche os espaços com o caractere entre ''


print('''Bem-vindo
Curso
lorem ippson 
sopa de letrinhas miúdas
javascript é melhor que python?
prof guanabara''') # se colocar aspas 3 vezes no inicio e no final do print escree o bloco de texto inteiro