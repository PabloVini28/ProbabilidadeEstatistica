# Morgado 2.6 - Questões - 11 questões resolvidas

from math import comb, factorial

# 1. Quantas são as soluções inteiras não-negativas de x + y + z + w = 3?
# Usamos a fórmula de combinações com repetição para encontrar o número de soluções.
n = 3  # Soma desejada
k = 4  # Número de variáveis

# Número de soluções inteiras não-negativas
x = comb(n + k - 1, k - 1)
print(x)

# 2. Quantas são as soluções inteiras não-negativas de x + y + z + w < 6?
# Usamos a fórmula de combinações com repetição para encontrar o número de soluções.
soma_total = 5  # Soma desejada
num_variaveis = 4  # Número de variáveis

# Número de soluções inteiras não-negativas para x + y + z + w <= 5
x = comb(soma_total + num_variaveis - 1, num_variaveis - 1)
print(x)

# 3. Quantas são as soluções inteiras positivas de x + y + z = 10?
# Usamos a fórmula de combinações para soluções inteiras positivas.
n = 10  # Soma desejada
k = 3   # Número de variáveis

# Número de soluções inteiras positivas
x = comb(n - 1, k - 1)
print(x)

# 4. Quantas são as soluções inteiras positivas de x + y + z < 10?
# Transformamos a desigualdade em uma equação equivalente para o cálculo.
soma_total = 6  # Soma desejada
num_variaveis = 3  # Número de variáveis

# Número de soluções inteiras positivas para x + y + z < 10
x = comb(soma_total + num_variaveis - 1, num_variaveis - 1)
print(x)

# 5. Quantas são as peças de um dominó comum?
# O número total de peças é dado pelo número de pares únicos de valores entre 0 e max_valor.
def calcular_pecas_dominio(max_valor):
    return (max_valor + 1) * (max_valor + 2) // 2

max_valor = 6  # Valor máximo no dominó
x = calcular_pecas_dominio(max_valor)
print(x)

# 7. De quantos modos podemos colocar em fila 7 letras A, 6 letras B e 5 letras C de modo que não haja duas letras B juntas?
from math import factorial

def contar_arranjos_com_restricoes(total_a, total_b, total_c):
    total_letras = total_a + total_b + total_c
    total_arranjos = factorial(total_letras) // (factorial(total_a) * factorial(total_b) * factorial(total_c))
    espacos_para_b = total_a + 1
    if total_b > espacos_para_b:
        return 0
    arranjos_b = factorial(espacos_para_b) // (factorial(total_b) * factorial(espacos_para_b - total_b))
    total_arranjos_com_restricoes = arranjos_b * (factorial(total_a + total_c) // (factorial(total_a) * factorial(total_c)))
    return total_arranjos_com_restricoes

letras_a = 7
letras_b = 6
letras_c = 5
x = contar_arranjos_com_restricoes(letras_a, letras_b, letras_c)
print(x)

# 8. Qual é o número máximo de termos de um polinômio homogêneo do grau p com n variáveis?
def numero_maximo_termos_polinomio(p, n):
    return comb(p + n - 1, n - 1)

grau = 3
variaveis = 4
x = numero_maximo_termos_polinomio(grau, variaveis)
print(x)

# 9. Qual é o número máximo de termos de um polinômio homogêneo do grau p com n variáveis?
n = 11  # Número de variáveis
p = 5   # Grau do polinômio

x = numero_maximo_termos_polinomio(p, n)
print(x)

# 10. Quantas caixas diferentes podem ser formadas com 8 tipos de bombons, sendo que cada caixa contém 30 bombons (do mesmo tipo ou sortidos)?
def calcular_caixas_diferentes(num_tipos, num_bombons):
    return comb(num_tipos + num_bombons - 1, num_bombons)

num_tipos = 8
num_bombons = 30
x = calcular_caixas_diferentes(num_tipos, num_bombons)
print(x)

# 11. De quantos modos podem ser pintados 10 objetos idênticos usando 3 cores diferentes?
def calcular_pinturas(num_objetos, num_cores):
    return comb(num_objetos + num_cores - 1, num_cores - 1)

num_objetos = 10
num_cores = 3
x = calcular_pinturas(num_objetos, num_cores)
print(x)

# 12. Quantos números inteiros entre 1 e 100.000 têm a soma dos algarismos igual a 6?
def contar_numeros_com_soma_algarismos(soma_desejada, num_digitos):
    def contar_solucoes(n, k):
        total = 0
        for i in range(0, n + 1):
            total += (-1)**i * comb(n, i) * comb(k - i * 10 + n - 1, n - 1)
        return total

    return contar_solucoes(num_digitos, soma_desejada)

num_digitos = 5
soma_desejada = 6
x = contar_numeros_com_soma_algarismos(soma_desejada, num_digitos)
print(x)
