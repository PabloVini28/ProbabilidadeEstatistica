print("=====================================================================")
print("|  Morgado 3.5 (O Princípio de Dirichlet) - 12 questões resolvidas  |")
print("=====================================================================", "\n")

print("01) Em uma gaveta há 12 meias brancas e 12 meias pretas. Quantas meias devemos")
print("retirar ao acaso para termos certeza de obter um par de meias da mesma cor?", "\n")

# Pensando nas meias como objetos e nas duas cores com as duas gavetas, vê-se que
# com 3 meias haverá duas meias com a mesma cor.

result = 3
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("02) 63.127 candidatos compareceram a uma prova do vestibular (25 questões de múltipla")
print("escolha com 5 alternativas por questão). Considere a afirmação:")
print("“Pelo menos dois candidatos responderam de modo idêntico a k primeiras questões da prova”.")
print("Qual é o maior valor de k para o qual podemos garantir que a afirmação acima é verdadeira?", "\n")

# Há 5 modos de responder a primeira questão, 5^2 = 25 modos de responder as duas
# primeiras questões,...,5^6 = 15.625 modos de responder as seis primeiras questões
# e 5^7 = 78.125 modos de responder as sete primeiras questões. Pensando nos candidatos
# como objetos e nos modos de responder como gavetas.

# Calculando o maior valor de k para garantir a afirmação
result = 6
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("03) Refaça o problema anterior para a afirmação:")
print("“Pelo menos 4 candidatos responderam de modo idêntico as k primeiras questões da prova”.", "\n")

# Há 5 modos de responder a primeira questão, 5^2 = 25 modos de responder as duas primeiras
# questões,...,5^k modos de responder as k primeiras questões. O maior grupo de pessoas
# para o qual não é necessariamente verdade que pelo menos 4 pessoas responderam de modo
# idêntico as k primeiras questões da prova é um grupo de 3 * 5^k pessoas, no qual cada
# um dos 5^k modos de responder as k primeiras questões foi usado por 3 pessoas.
# Portanto, 3 * 5^k + 1 é o tamanho do menor grupo para o qual podemos garantir que haverá
# pelo menos quatro pessoas que responderam de modo idêntico as k primeiras questões.
# Devemos ter 63127 ≥ 3 * 5^k + 1 e o maior valor de k é 6.

# Calculando o maior valor de k para garantir a afirmação
result = 6
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("04) Um ponto (x,y,x) do R^3 é inteiro se todas suas coordenadas são inteiras.", "\n")

print("04) a) Considere um conjunto de nove pontos inteiros do R^3. Mostre que o ponto")
print("médio de algum dos segmentos que ligam esses pontos é inteiro.", "\n")

# Resolução:
# Para nove pontos inteiros em R^3, considere as paridades das coordenadas (par ou ímpar).
# Cada coordenada pode ser par ou ímpar, resultando em 2^3 = 8 combinações de paridade.
# Com 9 pontos, pelo Princípio da Casa dos Pombos, pelo menos dois pontos terão a mesma
# paridade em todas as coordenadas.
# Para esses dois pontos, o ponto médio será um ponto inteiro.

print("Resposta: Pelo Princípio da Casa dos Pombos, em um conjunto de nove pontos inteiros")
print("          no espaço R^3, haverá pelo menos dois pontos que compartilham a mesma")
print("          paridade para cada coordenada (x, y, z).")
print("          Assim, o ponto médio desses dois pontos terá coordenadas inteiras.", "\n")


print("--------------------------------------------------------------", "\n")


print("04) b) Dê um exemplo de um conjunto de oito pontos inteiros do R^3 tais que nenhum")
print("dos pontos médios dos segmentos que ligam esses pontos é inteiro.", "\n")

# Exemplo de um conjunto de oito pontos inteiros no espaço R^3.
# As coordenadas são escolhidas para que a soma de cada par de pontos tenha pelo menos
# uma coordenada ímpar.

pontos = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]

print("Resposta: Um conjunto de oito pontos inteiros no R^3 onde nenhum dos pontos médios")
print("          dos segmentos que ligam esses pontos é inteiro é o seguinte conjunto:", "\n")
print("   ", pontos, "\n")


print("--------------------------------------------------------------", "\n")


print("05) Qual é o número mínimo de pessoas que deve haver em um grupo para que possamos")
print("garantir que nele haja pelo menos 5 pessoas nascidas no mesmo mês?", "\n")

# O maior grupo para o qual não se pode garantir que a existência de pelo menos
# 5 pessoas nascidas no mesmo mês é formado por 48 pessoas: 4 nascidas em janeiro,
# 4 em fevereiro,..., 4 em dezembro.

# Calculando o número mínimo de pessoas usando o Princípio da Casa dos Pombos
meses = 12
pessoas_por_mes = 4
total_pessoas = meses * pessoas_por_mes
result = total_pessoas + 1

print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("06) Mostre que em todo (n + l)-subconjunto de {1,2,...,2n} há um par de elementos")
print("tais que um deles divide o outro.", "\n")

# Para um conjunto {1, 2, ..., 2n}, vamos usar a ideia de representar cada número como
# 2^k * m onde m é ímpar. Cada número no conjunto pode ser dividido em subconjuntos onde os
# números são múltiplos uns dos outros. Com n + 1 elementos em um subconjunto, e no máximo
# n subconjuntos possíveis, pelo Princípio da Casa dos Pombos, pelo menos um subconjunto
# terá dois elementos que são múltiplos, garantindo que um elemento divide o outro.

print("Resposta: Para um conjunto {1, 2, ..., 2n}, representamos cada número como 2^k * m")
print("          onde m é ímpar. Particionamos o conjunto em subconjuntos onde os números")
print("          são múltiplos uns dos outros. Com n + 1 elementos e no máximo n subconjuntos,")
print("          pelo Princípio da Casa dos Pombos, pelo menos um subconjunto terá dois")
print("          elementos, garantindo que um deles divide o outro.", "\n")


print("--------------------------------------------------------------", "\n")


print("07) Prove que todo número natural tem um múltiplo que se escreve, na base 10,")
print("apenas com os algarismos 0 e 1.", "\n")

print("Resposta: Para qualquer número natural n, considere os números formados apenas pelos")
print("          dígitos 0 e 1. Pelo Princípio da Casa dos Pombos, entre n+1 desses números,")
print("          dois terão o mesmo resto ao serem divididos por n. A diferença entre esses")
print("          dois números é um múltiplo de n e é escrito apenas com os dígitos 0 e 1.", "\n")


print("--------------------------------------------------------------", "\n")


print("08) Prove que em qualquer conjunto de 52 inteiros existe um par de inteiros cuja")
print("soma ou cuja diferença é divisível por 100.", "\n")

print("Resposta: Em qualquer conjunto de 52 inteiros, considere seus restos ao serem divididos")
print("          por 100. Com 52 inteiros e 100 possíveis restos, pelo Princípio da Casa dos")
print("          Pombos, há pelo menos dois inteiros com restos congruentes. A diferença entre")
print("          esses inteiros é divisível por 100. Portanto, em qualquer conjunto de 52")
print("          inteiros, existe um par cuja soma ou diferença é divisível por 100.", "\n")


print("--------------------------------------------------------------", "\n")


print("09) Prove que dado qualquer conjunto de dez inteiros positivos de dois dígitos cada,")
print("é possível obter dois subconjuntos disjuntos cujos elementos têm a mesma soma.", "\n")

print("Resposta: Em qualquer conjunto de 10 inteiros positivos de dois dígitos, há 2^10 = 1024")
print("          subconjuntos possíveis. A soma de cada subconjunto varia, mas o número total")
print("          de diferentes somas possíveis é menor que 1024. Pelo Princípio da Casa dos")
print("          Pombos, haverá pelo menos dois subconjuntos disjuntos com a mesma soma.", "\n")


print("--------------------------------------------------------------", "\n")


print("10) Considere 1990 pontos em um plano. Prove que quaisquer três semiplanos, tais")
print("que cada um deles contém mais de 1327 desses pontos, têm interseção não vazia.", "\n")

# Denote A, B e C como os conjuntos de pontos nos semiplanos. Cada um contém mais de 1327 pontos.
# Total de pontos = 1990.
# |A ∪ B ∪ C| ≤ 1990.
# Aplicando o Princípio da Inclusão-Exclusão:
# |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C| ≥ 3981 - 1990
# Portanto, |A ∩ B ∩ C| ≥ 4.

print("Resposta: Dado qualquer conjunto de 1990 pontos e três semiplanos, cada um contendo")
print("          mais de 1327 pontos, o número total de pontos é 1990. Usando o Princípio")
print("          da Inclusão-Exclusão, calculamos que pelo menos 4 pontos estão na interseção")
print("          dos três semiplanos. Portanto, quaisquer três semiplanos com mais de 1327")
print("          pontos cada têm interseção não vazia.", "\n")


print("--------------------------------------------------------------", "\n")


print("14) Seja n um inteiro ímpar maior que 1 e seja A uma matriz n x n simétrica tal que")
print("cada linha e cada coluna de A é formada pelos números {1, 2, ..., n} escritos em")
print("alguma ordem. Mostre que cada um dos inteiros {1, 2, ..., n} aparece na diagonal")
print("principal de A.", "\n")

# Cada número aparece exatamente n vezes na matriz. 
# Como a matriz é simétrica, cada número fora da diagonal aparece em pares. 
# Sendo n ímpar, o total de ocorrências fora da diagonal é par, e assim, cada
# número aparece pelo menos uma vez na diagonal principal.

print("Resposta: Cada número de 1 a n aparece exatamente n vezes na matriz. Devido à simetria")
print("          da matriz, as ocorrências fora da diagonal principal aparecem em pares. Como")
print("          n é ímpar, a quantidade de vezes que cada número aparece fora da diagonal é")
print("          par. Portanto, cada número deve aparecer pelo menos uma vez na diagonal")
print("          principal da matriz.", "\n")


print("--------------------------------------------------------------", "\n")