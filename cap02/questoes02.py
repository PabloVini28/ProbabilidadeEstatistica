# Morgado 2.1 - Questões - 20 questões resolvidas


# 01 Quantas palavras contendo 3 letras diferentes podem ser formadas com 
#  um alfabeto de 26 letras?

x = 26
y = 25
z = 24
print(x*y*z)

# 02 Quantos são os gabaritos possíveis de um teste de 10 questões de múltiplas escolha, com cinco alternativas por questão?

x = 5
print(x**10)

# 03 Quantos inteiros há entre 1000 e 9999 cujos algarismos são distintos?

x = 9*9*8*7
print(x)

# 04 De quantos modos diferentes podem ser escolhidos um presidente e um
# secretário de um conselho que tem 12 membros?

x = 12 * 11
print (x);

#  05 De quantos modos 3 pessoas podem sentar-se em 5 cadeiras em fila?
x = 5*4*3
print(x)

# 06 a) Quantos números de quatro dígitos são maiores que 2400 e tem todos os digitos diferentes

x = 7*9*8*7
y = 1*6*8*7
print(x+y)

# 06 b) Quantos números de quatro dígitos são maiores que 2400 e não têm dígitos iguais a 3,5 ou 6.

x = 4*7*7*7
y= 1*4*7*7
print(x+y-1) # não contabiliza o 2400s

# 06 c) Quantos números de quatro dígitos são maiores que 2400 e têm as propriedades a) e b) simultaneamente.

x = 4*6*5*4
y = 4*5*4
print(x+y)

# 08) Quantos divisores naturais possui o número 360? Quantos são pares?

# 360 = 2^3 * 3^2 * 5
# (0,1,2,3) * (0,1,2) * (0,1) = 4*3*2 = 24
divisores = [1,2,3,4,5,6,8,9,10,12,15,18,20,24,30,36,40,45,60,72,90,120,180,360]
pares = [n for n in divisores if n%2 == 0]
qtd_divisores = len(divisores)
qtd_pares = len(pares)
print(qtd_divisores)
print(qtd_pares)

# 09) Quantos são os números naturais de 4 dígitos que possuem pelo menos dois dígitos iguais?
x = 9*10*10*10 # 4 digitos iguais
y = 9*9*8*7 # 4 digitos diferentes
print(x-y)

# 11)  De quantos modos podemos arrumar 8 torres iguais em um tabuleiro
# de xadrez (8 x 8) de modo que não haja duas torres na mesma linha nem na mesma coluna?
x = 8*7*6*5*4*3*2*1 # permutações de 8 elementos com repetição
print (x)

# 12)  Em uma banca há 5 exemplares iguais da revista A, 6 exemplares iguais
# da revista B e 10 exemplares iguais da revista C. Quantas coleções não vazias de revistas dessa banca é possível formar?

# x = 5*A + 6*B + 10*C = 300 # com três revista
# y = 5A + 10C = 50 # com duas revista
# z = 6B + 10C = 60 # com duas revistas
# w = 5A + 6B = 30 # com duas revistas
# u = 5,6,10 # com 5,6,10 revistas
x = 300 + 50 +60 +30 + 5 + 6 + 10
print(x)

# 13) Ee um baralho comum (52 cartas) sacam-se sucessivamente e sem reposição três cartas. Quantas são as extrações nas quais a primeira carta é
# de copas, a segunda é um rei e a terceira não é uma dama?

# Primeira extração - 1 rei de copas          # 1 dama de copas       # 11 modos
# Segunda extração - 3 reis restantes         # 4 modos restantes     # 4 modos
# Terceira extração - 46 cartas restantes     # 47 modos restantes    # 46 modos

x = 1*3*46 + 1*4*47 + 11*4*46
print (x)

# 14)  Quantos números diferentes podem ser formados multiplicando alguns (ou todos) dos números 1,5,6,7,7,9,9,9?
# 1 - 1 possibilidades
# 5 - 2 possibilidades
# 6 - 2 possibilidades
# 7 - 3 possibilidades
# 9 - 4 possibilidades
x = 1*2*2*3*4
print(x) 

# 15)  Um vagão de metrô tem 10 bancos individuais, sendo 5 de frente e 5 de
# costas. De 10 passageiros, 4 preferem sentar de frente, 3 preferem sentar de
# costas e os demais não têm preferência. De quantos modos os passageiros
# podem se sentar, respeitando-se as preferências?

# Frente - 5*4*3*2
# Costas - 5*4*3
# Nenhum - 3*2*1
x = 120*60*6
print(x)

# 17)  Quantos números inteiros entre 100 e 999 são ímpares e possuem três
# dígitos distintos?

count = 0
for num in range(100, 1000):
    digits = set(str(num))
    if num % 2 != 0 and len(digits) == 3:
        count += 1
print(count)

# 18) Escrevem-se os inteiros de 1 até 222 222. Quantas vezes o algarismo zero é escrito?
count = 0
for num in range(1, 222223):
    count += str(num).count('0')
print(count)

#  Quantos são os números de 5 algarismos, na base 10
# a) nos quais o algarismo 2 figura?
# b) nos quais o algarismo 2 não figura?
# Não aparece o 2 = 8*9*9*9*9 = 52488
# Aparece o 2 = 9*10*10*10*10 = 90000
a = 90000
b = 52488
print(a)
print(b)

# 20)  Em um concurso há três candidatos e cinco examinadores, devendo
# cada examinador votar em um candidato. De quantos modos os votos podem ser distribuídos?
x = 3*3*3*3*3
print(x)

# 21)  O código morse usa “palavras” contendo de 1 a 4 “letras”, as “letras”
# sendo ponto e traço. Quantas “palavras” existem no código morse?

# 1 letra = 2 sinais (ponto + traço)  
# 2 letras = 4 sinais (ponto + traço)
# 3 letras = 8 sinais (ponto + traço)
# 4 letras = 16 sinais (ponto + traço)
x = 2 + 4 + 8 + 16
print(x)

# 22) Fichas podem ser azuis, vermelhas ou amarelas; circulares, retangulares ou triangulares; finas ou grossas. Quantos tipos de fichas existem?
x = 3*3*2 
print(x)

# 24) No Senado Federal, o Distrito Federal e os 26 estados da federação têm
# 3 representantes cada. Deve-se formar uma comissão de modo que todos
# os estados e o Distrito Federal estejam representados por 1 ou 2 senadores.
# De quantos modos essa comissão pode ser formada?

# 1 senador = 27*26*25/2 = 13512
# 2 senadores = 27*26/2 = 351
x = 13512 + 351
print(x)

# 25 a) Qual é a soma dos divisores inteiros e positivos de 720?
def soma_divisores(n):
    soma = 0
    for i in range(1, n + 1):
        if n % i == 0:
            soma += i
    return soma

numero = 720
soma = soma_divisores(numero)
print(soma)







