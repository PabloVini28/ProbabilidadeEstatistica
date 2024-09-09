# Morgado 4.1 - Questões - 7 questões resolvidas
# 1 - prove fazendo as contas, a relação de Stifel : supondo que n um real qualquer e p inteiro não negativo

#   (n+1)!           =    n!           +   n!
#  (p+1)!(n+1-p-1)!       p!(n-p)!         (p+1)!(n-p-1)!

# (n+1) n! - (p+1) n! - (n-p) n! = 0

# 0 = 0

print('resolução no comentário da questão!')

# 3 - prove fazendo as contas que: //// supondo que n um real qualquer e p inteiro não negativo

#   (n+2)!           =    n!           +   2n!                  + n!
#  (p+2)!(n+2-p-2)!       p!(n-p)!         (p+1)!(n-p-1)!         (p+2)!(n-p-2)!

# n^2 + n + 2n + 2 = 2pn + p - p^2 + 4n + 2 - 2p + n^2 - pn - pn + p^2 - n + p

# 0 = 0

print('resolução no comentário da questão!')

# 4 - Usando a relação de Stifel, escreva as sete primeiras linhas do Triângulo de Pascal.

#mutcho texto, resumindo eu uso isso para descobrir : 

#   (n + 1)         =    n      +     n
#   (k + 1)              k           k+1

# 1
# 1 1
# 1 2 1 
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1

print('resolução no comentário da questão!')

# 6 - Dado que um conjunto possui 512 subconjuntos, qual é o número de elementos no conjunto?

# 2^n = 512        n = 9

x = 9

print(9)

# 7 - Determine um conjunto que possa ter exatamente 48 subconjuntos.

print('impossivel pois 48 não é potencia de 2')

# 10 - # Quantos coqueteis (misturas de duas ou mais bebidas) podem ser feitos a partir de 7 ingredientes distintos?

x = 2**7 - 1 - 1

print(x)

# 11 - Em uma sala há 7 lampadas. De quantas maneiras diferentes essas 7 lampadas podem ser acesas?

x = 2**7 - 1

print(x)



