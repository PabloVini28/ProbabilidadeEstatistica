# Morgado 5.3 - Questões - 9 questões resolvidas

# 1. Uma caixa contém 20 peças em boas condições e 15 em más condições.
# Uma amostra de 10 peças é extraída. Calcular a probabilidade de que ao menos uma peça na amostra seja defeituosa.

from math import comb

total_bom = 20
total_mal = 15
total_pecas = total_bom + total_mal
amostra = 10

total_combinacoes = comb(total_pecas, amostra)

if amostra <= total_bom:
    comb_boas = comb(total_bom, amostra)
else:
    comb_boas = 0

prob_nenhuma_defeituosa = comb_boas / total_combinacoes

x = 1 - prob_nenhuma_defeituosa

print(x)

# 5. Colocam-se aleatoriamente b bolas em b urnas. Calcular a probabilidade de que exatamente uma urna seja deixada desocupada.

urnas = 3
bolas = 5

total_maneiras = urnas ** bolas

maneiras_uma_vazia = urnas * ((urnas - 1) ** bolas)

x = maneiras_uma_vazia / total_maneiras

print(x)

# 6. Dez pessoas são separadas em dois grupos de 5 pessoas cada um.
# Qual é a probabilidade de que duas pessoas determinadas A e B façam parte do mesmo grupo?

total_divisoes = 1
for i in range(5):
    total_divisoes *= (10 - i)
    total_divisoes //= (i + 1)
total_divisoes //= 2 

maneiras_mesmo_groupo = 1
for i in range(3):
    maneiras_mesmo_groupo *= (8 - i)
    maneiras_mesmo_groupo //= (i + 1)

x = maneiras_mesmo_groupo / total_divisoes
print(x)

# 8. Um número entre 1 e 200 é escolhido aleatoriamente. Calcular a probabilidade de que seja divisível por 5 ou por 7.

total_numeros = 200

divisiveis_5 = total_numeros // 5
divisiveis_7 = total_numeros // 7
divisiveis_35 = total_numeros // 35

total_divisiveis = divisiveis_5 + divisiveis_7 - divisiveis_35
x = total_divisiveis / total_numeros
print(x)

# 9. Uma moeda foi cunhada de tal forma que é 4 vezes mais provável dar cara do que coroa.
# Calcular as probabilidades de cara e coroa.

x = 1 / (4 + 1)
y = 4 * x
print(x)
print(y)

# 10. Aos números inteiros entre 1 e n são designadas probabilidades proporcionais aos seus valores.
# Calcular P(i) para 1 <= i <= n.

n = 10
soma = sum(range(1, n + 1))
for i in range(1, n + 1):
    x = i / soma
    print(x)

# 11. Três dados são jogados simultaneamente. Calcular a probabilidade de obter 12 como soma dos resultados dos três dados.

total_combinacoes = 6 ** 3

combinacoes_12 = 0
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i + j + k == 12:
                combinacoes_12 += 1

x = combinacoes_12 / total_combinacoes

print(x)

# 12. Dois dados são jogados simultaneamente. Calcular a probabilidade de obter 7 como soma dos resultados.

total_combinacoes_dois_dados = 6 ** 2

combinacoes_7 = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == 7:
            combinacoes_7 += 1

x = combinacoes_7 / total_combinacoes_dois_dados
print(x)

# 14. Uma moeda equilibrada (probabilidade de cara = probabilidade de coroa = 1/2) é jogada n vezes.
# Calcular a probabilidade de obter exatamente k caras, 0 <= k <= n.

n = 5 
k = 3  

total_combinacoes = 1
for i in range(k):
    total_combinacoes *= (n - i)
    total_combinacoes //= (i + 1)

x = total_combinacoes * (0.5 ** n)
print(x)

