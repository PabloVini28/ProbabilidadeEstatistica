print("================================================================")
print("|  Morgado 3.2 (Permutações Caóticas) - 10 questões resolvidas  |")
print("================================================================", "\n")

print("01) a) Suponha #A = n. Quantas são as funções f : A -> A para as quais a")
print("equação f(x) = x não possui solução?", "\n")

# Cada elemento de A pode ter sua imagem escolhida de n modos.
print("Resposta: (n — 1)^n", "\n")


print("--------------------------------------------------------------", "\n")


print("01) b) Quantas são as funções f : A -> A bijetoras para as quais a equação")
print("f(x) = x não possui solução?", "\n")

# f(1), f(2), ..., f(n) deve ser uma permutação caótica de 1, 2, ..., n.
print("Resposta: Dn = n!( 1/0! - 1/1! + ... + (-1)^n/n! )", "\n")


print("--------------------------------------------------------------", "\n")


print("02) Quantas são as permutações de (1,2,3,4,5,6,7) que têm exatamente 3")
print("elementos no seu lugar primitivo?", "\n")

# O número de modos de escolher os três elementos que ocuparão o seu lugar primitivo
# é C'3'7 = 35. Postos estes elementos em seus lugares, os outros quatro elementos
# devem ser arrumados caoticamente, o que pode ser feito de D4 = 9 modos.

result = 35 * 9     #315
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("03) Determine o número de permutações caóticas de (1,2,3,4,5,6,7,8,9,10) nas")
print("quais os números 1,2,3,4,5 ocupam, em alguma ordem, os cinco primeiros lugares.", "\n")

# Os elementos 1, 2, 3, 4, 5 devem ser arrumados caoticamente nos 5 primeiros lugares,
# e os elementos 6, 7, 8, 9, 10 devem ser arrumados caoticamente nos 5 últimos lugares.
# D_5 * D-5 = 44 * 44
result = 44 * 44    #1.936
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("04) De quantos modos é possível colocar 8 torres brancas em um tabuleiro de")
print("xadrez 8 x 8 de modo que nenhuma torre fique na diagonal branca e não haja")
print("duas torres na mesma linha ou na mesma coluna?", "\n")

# Como são 8 torres e o tabuleiro é 8 x 8, em cada linha (e em cada coluna) do tabuleiro
# haverá uma única torre. Para colocar as torres, devemos escolher c(1) (coluna em que se
# encontra a torre da primeira linha), c(2),..., c(8). Ora, c(1), c(2),..., c(8) é uma
# permutação dos números 1, 2,..., 8. Para que nenhuma torre fique na diagonal branca,
# devemos ter c(1)≠1, c(2)≠2,...,c(8)≠8, ou seja, a permutação c(1), c(2),..., c(8) deve
# ser caótica.

from math import factorial

# Função para calcular o número de derangements (permutação caótica)
def derangement(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n - 1) * (derangement(n - 1) + derangement(n - 2))

# Número de permutações caóticas (derangements) de 8 elementos
n = 8
result = derangement(n)
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("05) Prove que, se n ≥ 3, D_n = (n - 1)( D_(n-1) + D_(n-2) ).", "\n")

# Nas permutações caóticas de 1,2,...,n, o elemento 1 não ocupa o primeiro lugar.
# As permutações caóticas de 1, 2 n podem ser divididas em duas categorias:
# - Primeira: permutações em que o elemento que ocupa o primeiro lugar tem seu lugar
# natural ocupado pelo 1;
# - Segunda: permutações em que o elemento que ocupa o primeiro lugar não tem seu lugar
# natural ocupado pelo 1.

# Para formar uma permutação de primeira categoria, devemos inicialmente escolher o elemento
# que ocupará o primeiro lugar e que terá seu lugar ocupado pelo 1; isso pode ser feito
# de n - 1 modos. Em seguida, devemos arrumar caoticamente os demais elementos, o que
# pode ser feito de modos.

# Para formar uma permutação de segunda categoria, devemos inicialmente escolher o elemento
# que ocupará o primeiro lugar, o que pode ser feito de n — 1 modos.

print("Resposta: O número de permutações de segunda categoria é (n-1)*D_(n-1).")
print("          Portanto, o número de permutações caóticas de 1, 2, ..., n é:")
print("          D_n  =  (n - 1)D_(n-2) + (n - 1)D_(n-1)  =  (n - 1)( D_(n-1) + D_(n-2).", "\n")


print("--------------------------------------------------------------", "\n")


print("06) Prove que (definindo D_0 = 1).")
print("       |n|         |n|             |n|                 |n|")
print("  n! = |0| D_n  +  |1| D_(n-1)  +  |2| D_(n-2) + ... + |n| D_0", "\n")

# O número de permutações de 1, 2, ..., n que têm exatamente k elementos no seu
# lugar original é C_n^k * D_(n-k).

print("Resposta: Como toda permutação tem 0, 1, 2, ... ou n elementos no lugar original,")
print("          Então: Σ(com k indo de 0 até n) C_n^k * D_(n-k)  é igual ao total de")
print("          permutações, ou seja, n! (valor dado no enunciado).", "\n")


print("--------------------------------------------------------------", "\n")


print("07) Prove que D_n = n*D_(n-1) + (—1)^n para n ≥ 2.", "\n")

print("Resposta: D_n  =  n! ( 1/0! - 1/1! + ... + (-1)^n / n! )")
print("               =  n! ( 1/0! - 1/1! + ... + (-1)^(n-1) / (n-1)! + (-1)^n / n! )")
print("               =  n(n-1)! ( 1/0! - 1/1! + ... + (-1)^(n-1) / (n-1)! ) + (-1)^n")
print("               =  n*D_(n-1) + (—1)^n", "\n")


print("--------------------------------------------------------------", "\n")


print("08) Dois médicos devem examinar, durante uma mesma hora, 6 pacientes, gastando 10")
print("minutos com cada paciente. Cada um dos 6 pacientes deve ser examinado pelos dois")
print("médicos. De quantos modos pode ser feito um horário compatível?", "\n")

# A agenda do primeiro médico pode ser montada de P_6 = 6! = 720 modos;
# E a do segundo, de D_6 = 265 modos.
# A resposta será = P_6 * D_6 

import math

def derangement(n):
    #Função que calcula o número de derangements (permutações caóticas) usando a
    # fórmula recursiva:
    # D_n = (n - 1) * (D_(n-1) + D_(n-2)).

    # Casos base
    if n == 0:
        return 1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Cálculo recursivo para n >= 3
    else:
        return (n - 1) * (derangement(n - 1) + derangement(n - 2))

# Número de pacientes
n = 6

# Permutações para o primeiro médico
P_n = math.factorial(n)

# Derangements para o segundo médico
D_n = derangement(n)

# Número total de modos compatíveis
result = P_n * D_n
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("09) Quantas são as permutações de (1, 2, ..., 2n) nas quais nenhum número ímpar")
print("ocupa o seu lugar primitivo?", "\n")

# Sejam A_1, A_2,...., A_n, respectivamente, os conjuntos das permutações em que o primeiro,
# o segundo,..., o n-ésimo número ímpar ocupam o seu lugar primitivo. Pelo Princípio da
# Inclusão-Exclusão, o número de elementos que não pertencem a nenhum dos conjuntos é:
#  a_0 = Σ(com k indo de 0 até n) (-1)^k * S_k  , sendo S_k a soma dos números de elementos
# das interseções de k dos conjuntos.

# Há C_n^k interseções de k dos conjuntos e cada uma delas possui (2n-k)! elementos. Logo:

print("Resposta: Σ(com k indo de 0 até n) (-1)^k * C_n^k (2n-k)!", "\n")


print("--------------------------------------------------------------", "\n")