# Morgado - 2.3 - Questões - 8 questões resolvidas

# 01) Uma comissão formada por 3 homens e 3 mulheres deve ser escolhida
# em um grupo de 8 homens e 5 mulheres.

# a) Quantas comissões podem ser formadas?
# 8!/(3!*5!) = 56
# 5!/3!*2! = 10
x = 56*10
print(x)

# b) Qual seria a resposta se um dos homens não aceitassem participar da
# comissão se nela estivesse determinada mulher?

# C 7-2 * C 2-4 = 21 * 6 = 126
x = 560 -126
print(x)

# . Para a seleção brasileira foram convocados dois goleiros, 6 zagueiros,
# 7 meios de campo e 4 atacantes. De quantos modos é possível escalar a
# seleção com 1 goleiro, 4 zagueiros, 4 meios de campo e 2 atacantes?

# C 1-2 * C 4-6 * C 4-7 * C 2-4 = 2 * 15 * 35 * 6 = 6300
x = 2 * 15 * 35 * 6
print(x)

# 04)  Quantas diagonais possui um polígono de n lados?
# C 2-n = n(n-1)/2
x = 5*(5-1)/2
print(x)

# 05)  Tem-se 5 pontos sobre uma reta R e 8 pontos sobre uma reta R' paralela
# a R. Quantos quadriláteros convexos com vértices em 4 desses 13 pontos
# existem?

# C 2-5 * C 2-8 = 10 * 28 = 280
x = 10 * 28
print(x)

# 06)  Em um torneio no qual cada participante enfrenta todos os demais uma
# única vez, são jogadas 780 partidas. Quantos são os participantes?

# n(n-1)/2 = 780
# n(n-1) = 1560
# n = 40
x = 40
print(x)

# 08)   Um homem tem 5 amigas e 7 amigos. Sua esposa tem 7 amigas e 5
# amigos. De quantos modos eles podem convidar 6 amigas e 6 amigos, se
# cada um deve convidar 6 pessoas?

# C 1/7 * C 5/7 * C 5/7 * C 1/5 = 7 * 21 * 21 * 5 = 5145
# C 2/5 * C 4/7 C 4/7 * C 2/5 = 10 * 35 * 35 * 10 = 122500
# C 3/5 * C 3/7 * C 3/7 * C 3/5 = 10 * 35 * 35 * 10 = 122500
# C 4/5 * C 2/7 * C 2/7 * C 4/5 = 5 * 21 * 21 * 5 = 11025
# C 5/5 * C 1/7 * C 1/7 * C 5/5 = 1 * 7 * 7 * 1 = 49
x = 5145 + 122500 + 122500 + 11025 + 49
print(x)

# 09)  Quantos são os números naturais de 7 dígitos nos quais o dígito 4 figura
# exatamente 3 vezes e o dígito 8 exatamente 2 vezes?
# algarismo para 2 espaços livres = 8^2
# C 3/7 * C 2/4 * 8^2 = 35 * 6 * 64 = 13440
x = 35 * 6 * 64
print(x)





