print("=============================================================================")
print("|  Morgado 3.1 (O Princípio da Inclusão-Exclusão) - 24 questões resolvidas  |")
print("=============================================================================", "\n")

print("01) Quantos inteiros entre 1 e 1000 inclusive:")

print("a) são divisíveis por pelo menos três dos números 2, 3, 7 e 10?", "\n")

# Para resolver esse problema, podemos usar o princípio da inclusão e exclusão.
# Primeiro, vamos encontrar quantos números são divisíveis por cada um dos
# quatro números dados: 2, 3, 7 e 10.

# Definindo os conjuntos e contando os elementos
S0 = 1000  # Total de números de 1 a 1000

# Números divisíveis por cada um dos números dados:
div_2 = 500
div_3 = 333
div_7 = 142
div_10 = 100

# Interseções de divisíveis por combinações de dois números
div_2_3 = 166
div_2_7 = 71
div_2_10 = 100
div_3_7 = 47
div_3_10 = 33
div_7_10 = 14

# Interseções de divisíveis por combinações de três números
div_2_3_7 = 23
div_2_3_10 = 33
div_2_7_10 = 14
div_3_7_10 = 4

# Divisíveis por todos os quatro números
div_2_3_7_10 = 4

# Aplicando o princípio da inclusão e exclusão
S1 = div_2 + div_3 + div_7 + div_10
S2 = div_2_3 + div_2_7 + div_2_10 + div_3_7 + div_3_10 + div_7_10
S3 = div_2_3_7 + div_2_3_10 + div_2_7_10 + div_3_7_10
S4 = div_2_3_7_10

# Calculando a quantidade de números divisíveis por pelo menos três dos quatro números
result = S3 - (3*S4)
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("01) b) não são divisíveis por nenhum dos números 2,3,7 e 10?", "\n")
result = S0 - S1 + S2 - S3 + S4
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("01) c) são divisíveis por exatamente um dos números 2,3,7 e 10?", "\n")
result = S1 - 2*S2 + 3*S3 - 4*S4
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("01) d) são divisíveis por pelo menos um dos números 2,3,7 e 10?", "\n")
result = S1 - S2 + S3 - S4
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("02) Quantos inteiros entre 1000 e 10000 inclusive não são divisíveis nem por 2,")
print("nem por 3 e nem por 5?", "\n")

# Definindo os conjuntos e contando os elementos
S0 = 10000 - 1000 + 1  # Total de números de 1000 a 10000

# Números divisíveis por cada um dos números dados:
div_2 = 4501  # Números pares entre 1000 e 10000
div_3 = 3000  # Números múltiplos de 3 entre 1000 e 10000
div_5 = 1801  # Números múltiplos de 5 entre 1000 e 10000

# Interseções de divisíveis por combinações de dois números
div_2_3 = 1500  # Múltiplos de 6
div_2_5 = 901  # Múltiplos de 10
div_3_5 = 600   # Múltiplos de 15

# Interseção de divisíveis por 2, 3 e 5
div_2_3_5 = 300  # Múltiplos de 30

# Aplicando o princípio da inclusão e exclusão
S1 = div_2 + div_3 + div_5
S2 = div_2_3 + div_2_5 + div_3_5
S3 = div_2_3_5

# Calculando a quantidade de números que não são divisíveis por nenhum dos três números
result = S0 - S1 + S2 - S3
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("03) Lançam-se 3 dados. Em quantos dos 6^3 resultados possíveis a soma dos pontos é 12?", "\n")

# Função para calcular combinações
def comb(n, k):
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    return comb(n-1, k-1) + comb(n-1, k)

# Total de soluções inteiras para a + b + c = 9
total_solucoes = comb(9 + 2, 2)  # C(11, 2) = 55

# Subtrair as soluções onde pelo menos uma variável é maior que 5
solucoes_invalidas = 0

for i in range(6, 10):  # i vai de 6 a 9
    soma_restante = 9 - i
    solucoes_invalidas += comb(soma_restante + 1, 1)  # C(soma_restante + 1, 1)

# Contar essas soluções 3 vezes
solucoes_invalidas *= 3

# Resultado final
combinacoes_validas = total_solucoes - solucoes_invalidas

print("Resposta:", combinacoes_validas, "\n")


print("--------------------------------------------------------------", "\n")


print("04) Quantas são as soluções inteiras não negativas de x + y + z = 12")
print("nas quais pelo menos uma incógnita é maior que 7?", "\n")

# Função para calcular combinações
def comb(n, k):
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    return comb(n-1, k-1) + comb(n-1, k)

# Soluções onde pelo menos uma incógnita é maior que 7
solucoes_maior_7 = 0

# Calcular as soluções onde x > 7.
# Para cada valor de x de 8 a 12, calculamos as soluções restantes para y + z.
for x in range(8, 13):
    solucoes_maior_7 += comb(12 - x + 1, 1)

# Como é impossível que haja mais de uma incógnita maior que 7,
# multiplicamos o resultado por 3 (uma para cada variável)
result = 3 * solucoes_maior_7

print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("05) Se #A = n e #B = p (n ≥ p), quantas são as funções f : A —> B sobrejetoras?", "\n")

from math import comb

# Definindo os valores de n e p
n = 5  # Exemplo: n = 5
p = 3  # Exemplo: p = 3

# Total de funções possíveis de A para B
total_funcoes = p ** n

# Funções que não são sobrejetivas
def calcular_nao_sobrejetivas(n, p):
    # Número de funções em que pelo menos um dos p elementos de B não está na imagem
    soma = 0
    for j in range(1, p + 1):
        # Número de funções em que exatamente j elementos não estão na imagem
        term = comb(p, j) * ((p - j) ** n)
        if j % 2 == 1:
            soma -= term
        else:
            soma += term
    return soma

# Calculando o número de funções sobrejetivas
funcoes_nao_sobrejetivas = calcular_nao_sobrejetivas(n, p)
funcoes_sobrejetivas = total_funcoes - funcoes_nao_sobrejetivas

result = funcoes_sobrejetivas
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("06) Determine o número de permutações de (1,2,3,4,5,6) nas quais")
print("nem o 4 ocupa o 4º lugar nem o 6 ocupa o 6º lugar.", "\n")

# Total de permutações
total_permutacoes = 6 * 5 * 4 * 3 * 2 * 1  # 6! = 720

# Permutações em que 4 ocupa o quarto lugar (5!)
perm_4_quarto = 5 * 4 * 3 * 2 * 1  # 5! = 120

# Permutações em que 6 ocupa o sexto lugar (5!)
perm_6_sexto = 5 * 4 * 3 * 2 * 1  # 5! = 120

# Permutações em que 4 ocupa o quarto lugar e 6 ocupa o sexto lugar (4!)
perm_4_quarto_6_sexto = 4 * 3 * 2 * 1  # 4! = 24

# Aplicando o princípio da inclusão e exclusão
result = total_permutacoes - perm_4_quarto - perm_6_sexto + perm_4_quarto_6_sexto

print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("07) a) Quantos são os inteiros de n dígitos, que têm todos os dígitos")
print("pertencentes ao conjunto {1,2,3}?", "\n")

# Cada uma das n casas pode ser preenchida de 3 modos
print("Resposta: 3^n", "\n")


print("--------------------------------------------------------------", "\n")


print("07) b) Em quantos deles os inteiros 1, 2 e 3 figuram todos?", "\n")

# Devemos subtrair do total os inteiros nos quais 1 não figura ou 2 não figura ou 3 não figura

# total = 3^n

# Calculando #(A), #(B), e #(C)
# A = 2^n  --> Inteiros em que 1 não figura
# B = 2^n  --> Inteiros em que 2 não figura
# C = 2^n  --> Inteiros em que 3 não figura

# Calculando #(A ∩ B), #(A ∩ C), e #(B ∩ C)
# A_inter_B = 1^n --> Inteiros em que 1 e 2 não figuram
# A_inter_C = 1^n --> Inteiros em que 1 e 3 não figuram
# B_inter_C = 1^n --> Inteiros em que 2 e 3 não figuram

# Calculando #(A ∩ B ∩ C)
# A_inter_B_inter_C = 0^n --> Inteiros em que 1, 2 e 3 não figuram

# Aplicando o princípio da inclusão e exclusão:

# 3^n - (A + B + C) + (A_inter_B + A_inter_C + B_inter_C) - A_inter_B_inter_C

# 3^n - 3*2^n + 3x1 - 0 = ...

print("Resposta: 3^n - 3 * 2^n + 3", "\n")


print("--------------------------------------------------------------", "\n")


print("08) Determine o número de permutações das letras AABBCCDD nas quais")
print("não há letras iguais adjacentes.", "\n")

import math

# Cálculo de permutações de AABBCCDD sem restrições
S0 = math.factorial(8) / (math.factorial(2) * math.factorial(2) * math.factorial(2) * math.factorial(2))

# Cálculo do número de permutações onde pelo menos duas letras iguais são adjacentes
# Número de permutações em que as duas letras A são adjacentes
S1 = 4 * (math.factorial(7) / (math.factorial(2) * math.factorial(2) * math.factorial(2)))

# Cálculo do número de permutações onde pelo menos duas letras iguais são adjacentes em dois pares diferentes
S2 = 6 * (math.factorial(6) / (math.factorial(2) * math.factorial(2)))

# Cálculo do número de permutações onde pelo menos duas letras iguais são adjacentes em três pares diferentes
S3 = 4 * (math.factorial(5) / math.factorial(2))

# Cálculo do número de permutações onde todas as letras são adjacentes
S4 = math.factorial(4)

# Aplicando o princípio da inclusão e exclusão para encontrar o número de permutações sem letras iguais adjacentes
result = S0 - S1 + S2 - S3 + S4

print("Resposta:", int(result), "\n")


print("--------------------------------------------------------------", "\n")


print("09) Quantos inteiros entre 1 e 1.000.000 não são nem quadrados perfeitos")
print("nem cubos perfeitos?", "\n")

# Definindo os conjuntos e contando os elementos
# A = conjunto dos quadrados perfeitos entre 1 e 1.000.000
# B = conjunto dos cubos perfeitos entre 1 e 1.000.000
# A ∩ B = conjunto das sextas potências perfeitas entre 1 e 1.000.000

# Número de quadrados perfeitos entre 1 e 1.000.000
num_quadrados_perfeitos = 1000  # 1^2, 2^2, ..., 1000^2

# Número de cubos perfeitos entre 1 e 1.000.000
num_cubos_perfeitos = 100  # 1^3, 2^3, ..., 100^3

# Número de sextas potências perfeitas entre 1 e 1.000.000
num_sextas_potencias = 10  # 1^6, 2^6, ..., 10^6

# Calculando a quantidade de números que são quadrados ou cubos perfeitos
num_A_union_B = num_quadrados_perfeitos + num_cubos_perfeitos - num_sextas_potencias

# Calculando a quantidade de números que não são nem quadrados nem cubos perfeitos
total_numeros = 1000000
result = total_numeros - num_A_union_B

print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("10) Determine o número de permutações de (1,2, ...,n) nas quais não figuram")
print("nem o par 12, nem o par 23, ..., nem o par (n - 1)n.", "\n")

def derangement(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n - 1) * (derangement(n - 1) + derangement(n - 2))

# Entrada
n = 5  # Exemplo, você pode alterar o valor de n conforme necessário

# Calculando o total de permutações de {1, 2, ..., n}
total_permutations = math.factorial(n)

# Calculando o número de permutações com nenhum par consecutivo na ordem dada
# Este é o derangement de n, D(n)
result = derangement(n)

print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("11) Oito crianças estão sentadas em tomo de um carrossel. De quantos modos")
print("elas podem trocar de lugar de modo que cada criança passe a ter")
print("uma criança diferente a sua direita?", "\n")

from math import comb

# Função para calcular permutações circulares sem pares adjacentes na ordem dada
def permutacoes_circulares_diferentes(n):
    S0 = math.factorial(n - 1)
    S1 = comb(n, 1) * math.factorial(n - 2)
    S2 = comb(n, 2) * math.factorial(n - 3)
    S3 = comb(n, 3) * math.factorial(n - 4)
    S4 = comb(n, 4) * math.factorial(n - 5)
    S5 = comb(n, 5) * math.factorial(n - 6)
    S6 = comb(n, 6) * math.factorial(n - 7)
    S7 = comb(n, 7) * math.factorial(n - 8)
    S8 = 1

    # Aplicando o princípio da inclusão e exclusão
    result = S0 - S1 + S2 - S3 + S4 - S5 + S6 - S7 + S8
    return result

# Número de crianças
n = 8

# Calculando o número de permutações circulares em que cada criança tem uma criança diferente à sua direita
result = permutacoes_circulares_diferentes(n)

print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("12) Calcule φ(360).", "\n")

# Decomposição de 360 em fatores primos
n = 360
fatores_primos = [2, 3, 5]

# Calculando φ(n) usando a fórmula
def phi(n, fatores_primos):
    resultado = n
    for p in fatores_primos:
        resultado *= (1 - 1/p)
    return int(resultado)

result = phi(n, fatores_primos)

print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("13) Quantas espécies de polígonos regulares de 100 lados existem?", "\n")

# Função para calcular o máximo divisor comum (MDC) entre dois números
# usando o algoritmo de Euclides
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Função para contar quantos números menores que n são coprimos (relativamente primos) com n
def count_coprimes(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:  # Se o MDC de i e n for 1, então são coprimos
            count += 1
    return count

n = 100

# Conta quantos números entre 1 e 99 são relativamente primos a 100
total_coprimes = count_coprimes(n)

# Divide por 2 para considerar apenas os números relativamente primos menores que 50
result = total_coprimes // 2

print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("14) Se p é um primo, quanto vale φ(p)?", "\n")

# Função para calcular φ(p) onde p é um número primo
def phi_prime(p):
    if p <= 1:
        raise ValueError("p deve ser um número primo maior que 1.")
    return p - 1  # Se p é primo, φ(p) é igual a p-1

# Exemplo de uso com um número primo
p = 7  # Substitua este valor pelo número primo desejado
result = phi_prime(p)

print("Resposta: φ(p) = p-1", "\n")


print("--------------------------------------------------------------", "\n")


print("15) Quantos são os elementos do conjunto {1,2, ...,500} que são divisíveis")
print("por 3 ou 5 mas não são divisíveis por 7?", "\n")

# Contagem de elementos divisíveis por 3
A1 = 500 // 3  # 166

# Contagem de elementos divisíveis por 5
A2 = 500 // 5  # 100

# Contagem de elementos divisíveis por 7
A3 = 500 // 7  # 71

# Contagem de elementos divisíveis por 15 (interseção de A1 e A2)
A1_inter_A2 = 500 // 15  # 33

# Contagem de elementos divisíveis por 21 (interseção de A1 e A3)
A1_inter_A3 = 500 // 21  # 23

# Contagem de elementos divisíveis por 35 (interseção de A2 e A3)
A2_inter_A3 = 500 // 35  # 14

# Contagem de elementos divisíveis por 105 (interseção de A1, A2 e A3)
A1_inter_A2_inter_A3 = 500 // 105  # 4

# Aplicando o princípio da inclusão e exclusão
total_div_3_or_5 = A1 + A2 - A1_inter_A2
total_div_3_or_5_not_7 = total_div_3_or_5 - (A1_inter_A3 + A2_inter_A3 - A1_inter_A2_inter_A3)

result = total_div_3_or_5_not_7  # 200

print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("16) a) De quantos modos podemos distribuir μ partículas distintas")
print("por n níveis distintos?", "\n")

# Há, para cada partícula, 𝑛 níveis distintos possíveis de serem ocupados, logo,
# a resposta é 𝑛 (escolha do nível da primeira partícula) vezes 𝑛 (escolha do nível da
# segunda partícula) vezes 𝑛 (escolha do nível da terceira partícula) ... vezes 𝑛 (escolha do
# nível da μ-ésima partícula).

print("Resposta: n^μ", "\n")


print("--------------------------------------------------------------", "\n")


print("16) b) Em quantas dessas distribuições todos os níveis ficam ocupados?", "\n")

# Em suma, queremos contar a quantidade de relações sobrejetivas de A (conjunto que
# representa as partículas) em B (conjunto que representa os níveis), sendo que 𝜇≥𝑛.

print("Resposta: Σ com k indo de 0 a n (-1)^k Cn^k (n - k)^μ", "\n")


print("--------------------------------------------------------------", "\n")


print("17) a) De quantos modos podemos distribuir μ partículas iguais")
print("por n níveis distintos?", "\n")

# Sejam x1 a quantidade de partículas associadas ao nível 1, x2 a quantidade de partículas
# associadas ao nível 2, etc. Para determinar tais quantidades, devemos resolver, em inteiros
# não negativos, a equação x1 + x2 +...+ xn = μ .

print("Resposta: (n + μ - 1)! / μ!(n - 1)!", "\n")


print("--------------------------------------------------------------", "\n")


print("17) b) Em quantas dessas distribuições todos os níveis ficam ocupados?", "\n")

# Agora desejamos o número de soluções inteiras e positivas de x1 + x2 +...+ xn = μ.
# Fazendo x1 = 1+y1 ,..., xn = 1+yn, a equação se transforma em y1 + y2 +...+ yn = μ — n, y1,y2,...,yn
# inteiros não negativos.

print("Resposta: (μ - 1)! / (μ - n)! (n - 1)!", "\n")


print("--------------------------------------------------------------", "\n")


print("18) De quantos modos podemos distribuir μ partículas iguais por n níveis")
print("distintos se nenhum nível pode conter mais de uma partícula?", "\n")

# Basta escolher, dos n níveis, os μ níveis que serão ocupados. A resposta será Cn^μ

print("Resposta: n! / μ!(n - μ)!", "\n")


print("--------------------------------------------------------------", "\n")