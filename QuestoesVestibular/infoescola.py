#LISTA QUESTÕES INFOESCOLA - PROBABILIDADE (15 QUESTÕES)
#1
# Um aluno prestou vestibular em apenas duas Universidades.
# Suponha que, em uma delas, a probabilidade de que ele seja aprovado é de 30%,
# enquanto na outra, pelo fato de a prova ter sido mais fácil, a probabilidade de sua aprovação sobe para 40%.
# Nessas condições, a probabilidade de que esse aluno seja aprovado em pelo menos uma dessas Universidades é de:

from math import comb

# Probabilidade de aprovação na primeira universidade
p1 = 0.30

# Probabilidade de aprovação na segunda universidade
p2 = 0.40

# Probabilidade de não ser aprovado em nenhuma das universidades
p_nao_1 = 1 - p1
p_nao_2 = 1 - p2

# Probabilidade de não ser aprovado em nenhuma das universidades
p_nao_ambas = p_nao_1 * p_nao_2

# Probabilidade de ser aprovado em pelo menos uma das universidades
p_ao_menos_uma = 1 - p_nao_ambas

# Printar a resposta
print(f"A probabilidade de ser aprovado em pelo menos uma das universidades é de {p_ao_menos_uma:.2f}")

# 2 (PUC-RIO 2010)
# Quatro moedas são lançadas simultaneamente.
# Qual é a probabilidade de ocorrer coroa em uma só moeda?

# Probabilidade de obter coroa em uma moeda
p_coroa = 0.5
# Probabilidade de obter cara em uma moeda
p_cara = 0.5

# Número total de resultados possíveis
total_resultados = 2 ** 4

# Número de maneiras de obter exatamente 1 coroa em 4 lançamentos
num_resultados_favoraveis = comb(4, 1)

# Probabilidade de obter exatamente 1 coroa em 4 lançamentos
probabilidade = num_resultados_favoraveis * (p_coroa ** 1) * (p_cara ** 3) / total_resultados

# Printar a resposta
print(f"A probabilidade de obter coroa em exatamente uma moeda é de {probabilidade:.2f}")

#3(PUC-RIO 2009)

# Jogamos dois dados comuns.
# Qual a probabilidade de que o total de pontos seja igual a 10?

# Número total de resultados possíveis ao lançar dois dados
total_resultados = 6 * 6  # Cada dado tem 6 faces, então 6 * 6 = 36 possíveis combinações

# Número de combinações que resultam em um total de 10 pontos
# As combinações possíveis são: (4,6), (5,5), (6,4)
resultados_favoraveis = 3

# Probabilidade de obter um total de 10 pontos
probabilidade = resultados_favoraveis / total_resultados

# Printar a resposta
print(f"A probabilidade de que o total de pontos seja igual a 10 é de {probabilidade:.2f}")

#4(PUC-RIO 2008)

# No jogo de Lipa sorteia-se um número entre 1 e 600 (cada número possui a mesma probabilidade).
# A regra do jogo é: se o número sorteado for múltiplo de 6 então o jogador ganha uma bola branca
# e se o número sorteado for múltiplo de 10 então o jogador ganha uma bola preta.
# Qual a probabilidade de o jogador não ganhar nenhuma bola?

# Número total de resultados possíveis
total_resultados = 600

# Números múltiplos de 6 entre 1 e 600
multiplo_6 = 600 // 6

# Números múltiplos de 10 entre 1 e 600
multiplo_10 = 600 // 10

# Números múltiplos de 6 e 10 (múltiplos de 30) entre 1 e 600
multiplo_6_e_10 = 600 // 30

# Número de números que são múltiplos de 6 ou múltiplos de 10
multiplo_6_ou_10 = multiplo_6 + multiplo_10 - multiplo_6_e_10

# Número de números que não são múltiplos nem de 6 nem de 10
nao_ganha_bola = total_resultados - multiplo_6_ou_10

# Probabilidade de não ganhar nenhuma bola
probabilidade = nao_ganha_bola / total_resultados

# Printar a resposta
print(f"A probabilidade de o jogador não ganhar nenhuma bola é de {probabilidade:.2f}")

#5(PUC-RIO 2008)

# A probabilidade de um casal com quatro filhos ter dois do sexo masculino e dois do sexo feminino é:

# Probabilidade de cada filho ser masculino ou feminino
p_masculino = 0.5
p_feminino = 0.5

# Número total de resultados possíveis ao ter 4 filhos
total_resultados = 2 ** 4  # Cada filho tem 2 possibilidades, então 2^4 = 16

# Número de maneiras de ter exatamente 2 filhos do sexo masculino e 2 do sexo feminino
num_resultados_favoraveis = comb(4, 2)

# Probabilidade de ter exatamente 2 filhos do sexo masculino e 2 do sexo feminino
probabilidade = num_resultados_favoraveis * (p_masculino ** 2) * (p_feminino ** 2) / total_resultados

# Printar a resposta
print(f"A probabilidade de um casal com quatro filhos ter dois do sexo masculino e dois do sexo feminino é de {probabilidade:.2f}")

#6(PUC-RIO 2007)

# A probabilidade de um dos cem números 1, 2, 3, 4, ..., 100 ser múltiplo de 6 e de 10 ao mesmo tempo é:

# Número total de resultados possíveis (números de 1 a 100)
total_resultados = 100

# Múltiplos de 6 e 10 simultaneamente são múltiplos do menor múltiplo comum, que é 30
multiplo_30 = 100 // 30

# Probabilidade de um número ser múltiplo de 30
probabilidade = multiplo_30 / total_resultados

# Printar a resposta
print(f"A probabilidade de um número entre 1 e 100 ser múltiplo de 6 e de 10 ao mesmo tempo é de {probabilidade:.2f}")

#8(UFMG 2008)

# Considere uma prova de Matemática constituída de quatro questões de múltipla escolha, com quatro alternativas cada uma,
# das quais apenas uma é correta. Um candidato decide fazer essa prova escolhendo, aleatoriamente, uma alternativa em cada questão.
# Então, é CORRETO afirmar que a probabilidade de esse candidato acertar, nessa prova, exatamente uma questão é:

# Número total de alternativas por questão
alternativas_por_questao = 4

# Probabilidade de acertar uma questão
p_acertar = 1 / alternativas_por_questao

# Probabilidade de errar uma questão
p_errar = 1 - p_acertar

# Número total de questões
total_questoes = 4

# Número de maneiras de acertar exatamente uma questão em 4
num_resultados_favoraveis = comb(total_questoes, 1)

# Probabilidade de acertar exatamente uma questão e errar as outras
probabilidade = num_resultados_favoraveis * (p_acertar ** 1) * (p_errar ** (total_questoes - 1))

# Printar a resposta
print(f"A probabilidade de acertar exatamente uma questão é de {probabilidade:.2f}")

#9(FUVEST 2009)

# Dois dados cúbicos, não viciados, com faces numeradas de 1 a 6, serão lançados simultaneamente.
# A probabilidade de que sejam sorteados dois números consecutivos, cuja soma seja um número primo, é de:

# Números primos possíveis para a soma dos dois dados
numeros_primos = {2, 3, 5, 7, 11}

# Número total de combinações possíveis ao lançar dois dados
total_combinacoes = 6 * 6  # Cada dado tem 6 faces, então 6 * 6 = 36 combinações

# Contar o número de combinações favoráveis
combinacoes_favoraveis = 0

# Verificar combinações de números consecutivos
for i in range(1, 6):  # Os números consecutivos possíveis são 1-2, 2-3, 3-4, 4-5, 5-6
    if (i + (i + 1)) in numeros_primos:
        combinacoes_favoraveis += 2  # (i, i+1) e (i+1, i) são ambas válidas

# Probabilidade de sorteio de números consecutivos cuja soma é um número primo
probabilidade = combinacoes_favoraveis / total_combinacoes

# Printar a resposta
print(f"A probabilidade de que sejam sorteados dois números consecutivos cuja soma seja um número primo é de {probabilidade:.2f}")

#10(ADVISE 2009)


# Número total de pessoas na empresa
total_pessoas = 35 + 15

# Número de homens
homens = 20

# Número de prestadores de serviço
prestadores_servico = 15

# Número de homens prestadores de serviço
homens_prestadores_servico = prestadores_servico - 5  # Total prestadores de serviço - mulheres prestadoras de serviço

# Número de pessoas que são homens ou prestadores de serviço
# Usamos o princípio da inclusão-exclusão para evitar contagem dupla
pessoas_homem_ou_prestador = homens + prestadores_servico - homens_prestadores_servico

# Probabilidade de escolher uma pessoa que seja homem ou prestador de serviço
probabilidade = pessoas_homem_ou_prestador / total_pessoas

# Printar a resposta
print(f"A probabilidade de uma pessoa escolhida aleatoriamente ser homem ou prestador de serviço é de {probabilidade:.2f}")

#11 (UFPR 2010)

# Em uma população de aves, a probabilidade de um animal estar doente é 1/25.
# Quando uma ave está doente, a probabilidade de ser devorada por predadores é 1/4,
# e, quando não está doente, a probabilidade de ser devorada por predadores é 1/40.
# Portanto, a probabilidade de uma ave dessa população, escolhida aleatoriamente, ser devorada por predadores é de:

# Probabilidade de uma ave estar doente
p_doente = 1 / 25

# Probabilidade de uma ave não estar doente
p_nao_doente = 1 - p_doente

# Probabilidade de uma ave doente ser devorada por predadores
p_devora_dado_doente = 1 / 4

# Probabilidade de uma ave não doente ser devorada por predadores
p_devora_dado_nao_doente = 1 / 40

# Probabilidade total de uma ave ser devorada por predadores
p_devora_total = (p_doente * p_devora_dado_doente) + (p_nao_doente * p_devora_dado_nao_doente)

# Printar a resposta
print(f"A probabilidade de uma ave ser devorada por predadores é de {p_devora_total:.4f}")

#12 (UFPR 2009)

# A linha de produção de uma fábrica produz milhares de peças por dia e apresenta, em média, quatro peças defeituosas a cada cem peças produzidas.
# Um inspetor de qualidade sorteia cinco peças de modo aleatório e verifica a quantidade de peças defeituosas.

# Parâmetros
probabilidade_defeito = 4 / 100  # Probabilidade de uma peça ser defeituosa
n = 5  # Número de peças sorteadas

# Função para calcular a probabilidade de ter exatamente k peças defeituosas entre 5
def probabilidade_defeituosas(k):
    return comb(n, k) * (probabilidade_defeito ** k) * ((1 - probabilidade_defeito) ** (n - k))

# Exemplo de cálculos para diferentes números de peças defeituosas
resultados = {}
for k in range(6):  # k pode variar de 0 a 5
    resultados[k] = probabilidade_defeituosas(k)

# Printar as probabilidades
for k, prob in resultados.items():
    print(f"A probabilidade de ter exatamente {k} peças defeituosas entre 5 peças sorteadas é de {prob:.4f}")

#15 (Enem 2011)

# Em um jogo de sinuca com 16 bolas (1 branca e 15 coloridas, com valores de 1 a 15 pontos),
# um jogador deve acertar duas bolas coloridas cujas somas correspondam a um número escolhido antes da jogada.
# Arthur, Bernardo e Caio escolhem os números 12, 17 e 22, respectivamente.
# O objetivo é determinar quem tem a maior probabilidade de ganhar o jogo.

# Valores das bolas coloridas
valores_bolas = list(range(1, 16))

# Função para calcular a soma das combinações de duas bolas
def contar_combinacoes(valor_desejado):
    contagem = 0
    for i in range(len(valores_bolas)):
        for j in range(i + 1, len(valores_bolas)):
            if valores_bolas[i] + valores_bolas[j] == valor_desejado:
                contagem += 1
    return contagem

# Contar combinações para os valores escolhidos por Arthur, Bernardo e Caio
soma_12 = contar_combinacoes(12)
soma_17 = contar_combinacoes(17)
soma_22 = contar_combinacoes(22)

# Número total de combinações possíveis ao escolher duas bolas de 15
total_combinacoes = comb(15, 2)

# Calcular as probabilidades de cada jogador ganhar
probabilidade_12 = soma_12 / total_combinacoes
probabilidade_17 = soma_17 / total_combinacoes
probabilidade_22 = soma_22 / total_combinacoes

# Determinar quem tem a maior probabilidade
maior_probabilidade = max(probabilidade_12, probabilidade_17, probabilidade_22)

# Determinar o jogador com a maior probabilidade
if maior_probabilidade == probabilidade_12:
    jogador = 'Arthur'
elif maior_probabilidade == probabilidade_17:
    jogador = 'Bernardo'
else:
    jogador = 'Caio'

# Printar as probabilidades e o resultado
print(f"Probabilidade de Arthur ganhar (soma = 12): {probabilidade_12:.4f}")
print(f"Probabilidade de Bernardo ganhar (soma = 17): {probabilidade_17:.4f}")
print(f"Probabilidade de Caio ganhar (soma = 22): {probabilidade_22:.4f}")
print(f"O jogador com a maior probabilidade de ganhar é {jogador}.")


#19 (UFRGS 2017)

#Considere um hexágono convexo com vértices A, B, C, D, E e F. Tomando dois vértices ao acaso, a probabilidade de eles serem extremos de uma diagonal do hexágono é:

# Número de vértices do hexágono
n = 6

# Número total de combinações de dois vértices
total_combinacoes = comb(n, 2)

# Número de diagonais de um hexágono
# O número total de diagonais em um polígono de n lados é dado por n * (n - 3) / 2
num_diagonais = n * (n - 3) // 2

# Probabilidade de que dois vértices escolhidos ao acaso sejam extremos de uma diagonal
probabilidade = num_diagonais / total_combinacoes

# Printar a resposta
print(f"A probabilidade de que dois vértices escolhidos ao acaso sejam extremos de uma diagonal é de {probabilidade:.4f}")

#20 (UFRGS 2016)

#No jogo de xadrez, cada jogador movimenta as peças de uma cor: brancas ou pretas. Cada jogador dispõe de oito peões, duas torres, dois cavalos, dois bispos, um rei e uma rainha.

#Escolhendo ao acaso duas peças pretas, a probabilidade de escolher dois peões é de:

# Número total de peças pretas
total_pecas_pretas = 8 + 2 + 2 + 2 + 1 + 1

# Número de peões pretos
num_peoes_pretos = 8

# Número total de combinações de escolher 2 peças entre as peças pretas
total_combinacoes = comb(total_pecas_pretas, 2)

# Número de combinações de escolher 2 peões entre os peões pretos
combinacoes_peoes = comb(num_peoes_pretos, 2)

# Probabilidade de escolher 2 peões
probabilidade_peoes = combinacoes_peoes / total_combinacoes

# Printar a resposta
print(f"A probabilidade de escolher duas peças pretas sendo ambas peões é de {probabilidade_peoes:.4f}")

#21 (UFRGS 2015)

#Um jogo consiste em responder corretamente a perguntas sorteadas, ao girar um ponteiro sobre uma roleta numerada de 1 a 10, no sentido horário. O número no qual o ponteiro parar corresponde à pergunta a ser respondida. A cada número corresponde somente uma pergunta, e cada pergunta só pode ser sorteada uma vez. Caso o ponteiro pare sobre um número que já foi sorteado, o participante deve responder a próxima pergunta não sorteada, no sentido horário.

#Em um jogo, já foram sorteadas as perguntas 1, 2, 3, 5, 6, 7 e 10. Assim, a probabilidade de que a pergunta 4 seja a próxima a ser respondida é de:


# Perguntas já sorteadas
perguntas_sorteadas = {1, 2, 3, 5, 6, 7, 10}

# Total de perguntas na roleta
total_perguntas = 10

# Perguntas restantes
perguntas_restantes = [i for i in range(1, total_perguntas + 1) if i not in perguntas_sorteadas]

# Número de perguntas restantes
num_restantes = len(perguntas_restantes)

# Verificar a posição da pergunta 4 na lista de perguntas restantes
# Encontrar a posição da pergunta 4 na lista de perguntas restantes
if 4 in perguntas_restantes:
    posicao_pergunta_4 = (perguntas_restantes.index(4) + 1) % num_restantes
    probabilidade = 1 / num_restantes
else:
    posicao_pergunta_4 = None
    probabilidade = 0

# Printar a resposta
print(f"A probabilidade de a pergunta 4 ser a próxima a ser respondida é de {probabilidade:.4f}")


