print("===================================================================")
print("|  Morgado 3.4 (O Princípio da Reflexão) - 6 questões resolvidas  |")
print("===================================================================", "\n")

print("01) Numa fila de cinema, m pessoas tem notas de R$ 5,00 e n(n < m) pessoas tem")
print("notas de R$ 10,00. A entrada custa R$ 5,00.", "\n")

print("01) a) Quantas são as filas possíveis?", "\n")

# O número de maneiras de permutar m pessoas com notas de R$ 5,00 e n pessoas com notas
# de R$ 10,00 é simplesmente o número de permutações dos (m + n) pessoas.
print("Resposta: P_(m+n) = (m + n)!", "\n")


print("--------------------------------------------------------------", "\n")


print("01) b) Quantas são as filas que terão problemas de troco se a bilheteria começa")
print("a trabalhar sem troco?", "\n")

# Façamos um gráfico, como o das eleições, pondo, no eixo y, a quantidade de nota de
# R$5,00 em poder da bilheteria e, no eixo x, a quantidade de pessoas atendidas.
# Os gráficos das filas são caminhos de (0, 0) a (m + n, m - n). Os que representam filas
# com problemas de troco são as que tocam a reta y = -1. Estes, refletindo-se na reta
# y = -1 o trecho de (0,0) até o primeiro toque na reta, correspondem biunivocamente aos
# caminhos de (0,-2) a (m+n, m-n).
# Tais caminhos são formados por subidas e descidas de modo que
# S + D = m+n  e  S - D = m-n + 2 , ou seja,
# S = m+1  e  D = n-1 .
# A escolha do caminho fixa, na fila, os lugares que serão ocupados pelos portadores de
# notas de R$5,00 e de notas de R$10,00. Fixados tais lugares, há m!n! modos de
# designar-lhe as pessoas.

print("Resposta: n/(m+1) * (m + n)!", "\n")


print("--------------------------------------------------------------", "\n")


print("01) c) Quantas são as filas que terão problemas de troco se a bilheteria começa")
print("a trabalhar com duas notas de R$ 5,00?", "\n")

# Agora, os gráficos são caminhos de (0,2) e (m+n, m-n+2). Os que representam filas
# com problemas de troco são os que tocam a reta y = -1. Estes, refletindo-se na reta
# y = -1 o trecho de (0,0) até o primeiro toque na reta, correspondem biunivocamente
# aos caminhos de (0,-4) e (m+n, m-n+2). Tais caminhos são formados por subidas e descidas
# de modo que S + D = m+n  e  S — D = m-n+6, ou seja, S = m+3 e D = n-3.

print("Resposta: n(n-1)(n-2) / (m+1)(m+2)(m+3) * (m+n)", "\n")


print("--------------------------------------------------------------", "\n")


print("02) Numa eleição com dois candidatos A e B, há 20 eleitores e o candidato A vence")
print("por 15 x 5. Quantas são as marchas da apuração:", "\n")

print("02) a) Possíveis?", "\n")

import math

# Função para calcular combinações
def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Número total de caminhos possíveis
total_caminhos = comb(20, 5)

result = total_caminhos     # 15.504
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("02) b) Nas quais o candidato A permanece em vantagem (nem sequer empata) desde")
print("o primeiro voto apurado?", "\n")

import math

# Função para calcular combinações
def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Total de caminhos de (0,0) a (20,10)
total_caminhos = comb(19, 5)

# Caminhos de (1,-1) a (20,10) que tocam y=0
caminhos_que_tocam = comb(19, 4)

# Caminhos válidos
caminhos_validos = total_caminhos - caminhos_que_tocam

result = caminhos_validos   #7.752
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("02) c) Nas quais o candidato A permanece sempre em vantagem ou empatado com")
print("o candidato B?", "\n")

import math

# Função para calcular o número de combinações
def combinacoes(n, k):
    return math.comb(n, k)

# Número total de caminhos possíveis de (0,0) a (20,10)
# Corrigindo para usar 30 votos (total de passos) e 10 passos positivos
total_caminhos = 15504

# Número de caminhos inválidos que tocam a reta y = -1
# Refletimos esses caminhos para (0, -2) a (20, 10)
invalidos = combinacoes(20, 4)

# Número de caminhos válidos
validos = total_caminhos-invalidos

print("Resposta:", validos, "\n")


print("--------------------------------------------------------------", "\n")