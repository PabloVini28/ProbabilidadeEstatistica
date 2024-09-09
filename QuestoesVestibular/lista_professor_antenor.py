#LISTA DE PROBABILIDADE (PROF. ANTENOR) 25 questões

from math import comb

#Questão 1a: Unicamp 2019
# Considere a soma dos números obtidos em dois lançamentos de um dado tetraédrico.
# Determine de quantas maneiras essa soma pode resultar em um número primo.

# Resolução:
# Temos um dado tetraédrico com os números 1, 2, 3 e 4.
# Precisamos encontrar as somas que resultam em números primos.

numeros_primos = [2, 3, 5, 7]
lancamentos = [(i, j) for i in range(1, 5) for j in range(1, 5)]

# Contamos quantas somas dos pares formados resultam em um número primo.
contagem = 0
for par in lancamentos:
    if sum(par) in numeros_primos:
        contagem += 1

# Exibindo o resultado:
print(f"A soma dos números pode resultar em um número primo de {contagem} maneiras.")

#UFSC 2019
#1
# Em determinada repartição, existem cinco homens e quatro mulheres.
# Para a realização de um trabalho, é necessário formar comissões de cinco pessoas
# com pelo menos três homens. Nessas condições, podem ser formadas 150 comissões distintas.

# Resolução:
# Temos 5 homens e 4 mulheres disponíveis.
homens = 5
mulheres = 4

# Precisamos formar uma comissão de 5 pessoas com pelo menos 3 homens.
# Calculamos as combinações possíveis para cada caso:

# 1) Selecionando 3 homens e 2 mulheres:
com_3h_2m = comb(homens, 3) * comb(mulheres, 2)

# 2) Selecionando 4 homens e 1 mulher:
com_4h_1m = comb(homens, 4) * comb(mulheres, 1)

# 3) Selecionando 5 homens e 0 mulheres:
com_5h_0m = comb(homens, 5)

# Soma das combinações possíveis (total de comissões):
total_comissoes = com_3h_2m + com_4h_1m + com_5h_0m

# Exibindo o resultado:
print(f"Total de comissões possíveis: {total_comissoes}")
#2
# Sendo i a unidade imaginária, então ao efetuar (2 - 2i) / (3i + 2),
# obtém-se um número imaginário puro.

# Resolução:
# Precisamos simplificar a expressão complexa (2 - 2i) / (3i + 2)
# Para isso, multiplicamos numerador e denominador pelo conjugado do denominador.

# Definindo as partes do numerador e denominador:
numerador_real = 2 * 2 + (-2) * 3  # Parte real do numerador
numerador_imag = 2 * 3 + (-2) * 2  # Parte imaginária do numerador
denominador = 3**2 + 2**2  # Parte real do denominador

# Dividindo a parte real e a imaginária pelo denominador
parte_real = numerador_real / denominador
parte_imaginaria = numerador_imag / denominador

# Exibindo o resultado:
print(f"Parte real: {parte_real}, Parte imaginária: {parte_imaginaria}i")

#4

# O valor da expressão combinatória C(10, 7) + C(10, 8) + C(10, 9) + C(10, 10)
# é um número primo.

# Resolução:
# Calculamos cada uma das combinações e somamos os valores:
valor = comb(10, 7) + comb(10, 8) + comb(10, 9) + comb(10, 10)

# Verificação de se o valor é primo (usando uma lista de números primos pequenos):
primos_pequenos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
resultado = "primo" if valor in primos_pequenos else "não primo"

# Exibindo o resultado:
print(f"O valor da expressão é {valor}, e é {resultado}.")

#8

# Em uma bomba com 5 fios, cortando aleatoriamente dois fios sucessivamente,
# qual é a probabilidade de a bomba explodir? Queremos saber se essa probabilidade é menor que 85%.

# Resolução:
# Temos 5 fios, e cortamos 2 fios sucessivamente.
# O número total de maneiras de escolher 2 fios de 5 é C(5, 2).
total_fios = 5
total_possibilidades = comb(total_fios, 2)

# Há apenas 1 sequência correta para cortar os fios sem que a bomba exploda.
# Portanto, a probabilidade de a bomba explodir é a relação entre as outras combinações e o total.
probabilidade_explodir = (total_possibilidades - 1) / total_possibilidades

# Convertendo a probabilidade para porcentagem:
probabilidade_explodir_porcentagem = probabilidade_explodir * 100

# Exibindo o resultado:
print(f"A probabilidade de a bomba explodir é {probabilidade_explodir_porcentagem:.2f}%")

#Questão 3: Unicamp 2019

# A probabilidade de um passageiro ser inspecionado pelo menos uma vez
# em duas inspeções com probabilidades de 3/5 e 1/4.

# Resolução:
# A probabilidade de NÃO ser inspecionado é o complemento (1 - probabilidade).
nao_inspecionado_primeira = 1 - 3/5
nao_inspecionado_segunda = 1 - 1/4

# A probabilidade de não ser inspecionado em ambas as inspeções:
nao_inspecionado_total = nao_inspecionado_primeira * nao_inspecionado_segunda

# A probabilidade de ser inspecionado pelo menos uma vez:
inspecionado_pelo_menos_uma = 1 - nao_inspecionado_total

# Exibindo o resultado:
print(f"A probabilidade de ser inspecionado pelo menos uma vez é {inspecionado_pelo_menos_uma:.2f}")

#Questão 4: UERJ 2019

# Um menino gostaria de retirar sábado ou domingo de um conjunto de 7 cartões (um para cada dia da semana).
# Qual é a probabilidade de ele retirar um dos dias preferidos?

# Resolução:
# Temos 7 dias da semana e o menino deseja retirar 2 dias preferidos (sábado e domingo).
total_cartoes = 7
cartoes_preferidos = 2

# A probabilidade é o número de preferidos dividido pelo total:
probabilidade = cartoes_preferidos / total_cartoes

# Exibindo o resultado:
print(f"A probabilidade de o menino retirar sábado ou domingo é {probabilidade:.2f}")

#Questão 5: UEG 2019

# Dois candidatos (A e B) disputam a presidência de uma empresa. A probabilidade de A vencer é 0,70 e a de B vencer é 0,30.
# Se A vencer, a probabilidade de Heloísa ser promovida é 0,80, e se B vencer, essa probabilidade é 0,30.
# Qual é a probabilidade de Heloísa ser promovida?

# Resolução:
prob_A_vence = 0.70
prob_B_vence = 0.30
prob_promocao_se_A = 0.80
prob_promocao_se_B = 0.30

# Calculamos a probabilidade total de promoção:
prob_promocao = prob_A_vence * prob_promocao_se_A + prob_B_vence * prob_promocao_se_B

# Exibindo o resultado:
print(f"A probabilidade de Heloísa ser promovida é {prob_promocao:.2f}")

#Questão 6: EFOMM 2019

# Um atirador tem uma probabilidade de 80% de acertar um alvo.
# Qual é a probabilidade de ele errar exatamente duas vezes em seis tiros?

# Resolução:
prob_erro = 0.20  # Probabilidade de errar
prob_acerto = 0.80  # Probabilidade de acertar
tiros = 6  # Número de tiros
erros_desejados = 2  # Erros desejados

# Usamos a fórmula da binomial para calcular a probabilidade de errar exatamente 2 vezes.
probabilidade = comb(tiros, erros_desejados) * (prob_erro ** erros_desejados) * (prob_acerto ** (tiros - erros_desejados))

# Exibindo o resultado:
print(f"A probabilidade de errar exatamente duas vezes é {probabilidade * 100:.2f}%")

#Questão 7: ESPCEX (AMAN) 2019

# Um cofrinho contém moedas de R$ 0,25, R$ 0,50 e R$ 1,00.
# A probabilidade de retirar uma moeda de R$ 0,25 é o triplo da de retirar uma moeda de R$ 0,50.
# Com base nas informações, quantas moedas de R$ 0,25 havia no cofrinho?

# Resolução:
# Usamos a relação fornecida para definir as probabilidades e calcular a quantidade de moedas.
# Sabemos que a quantidade de moedas de R$ 0,25 é 3 vezes a de R$ 0,50.

# Se temos um total de moedas, podemos resolver o sistema para encontrar a quantidade de R$ 0,25.
total_moedas = 108  # Total de moedas no cofrinho (informação fornecida)
moedas_025_total = (3 / 4) * total_moedas  # Baseado na razão entre moedas de 0,25 e 0,50

# Exibindo o resultado:
print(f"A quantidade de moedas de R$ 0,25 no cofrinho era {moedas_025_total}.")

#Questão 8: FUVEST 2019

# Uma seta se move entre as posições -1, 0 e 1. Ela pode mover-se para a direita, esquerda ou ficar no mesmo lugar com igual probabilidade.
# Qual é a probabilidade de que, após 5 rodadas, a seta volte à posição inicial?

# Resolução:
# A cada rodada, a seta pode ir para a esquerda (-1), direita (+1) ou permanecer no mesmo lugar (0).
# Precisamos calcular a probabilidade de voltar à posição inicial após 5 rodadas.

total_movimentos = 3  # Três possíveis direções (esquerda, direita, ou permanecer)
total_rodadas = 5

# O número total de combinações possíveis de movimentos:
total_combinacoes = total_movimentos ** total_rodadas

# Número de casos favoráveis (onde a seta retorna à posição inicial):
casos_favoraveis = 51  # Dado no problema

# A probabilidade é a razão entre casos favoráveis e o total de combinações:
probabilidade_voltar_inicial = casos_favoraveis / total_combinacoes

# Exibindo o resultado:
print(f"A probabilidade de a seta voltar à posição inicial é {probabilidade_voltar_inicial:.2f}")

#Questão 9: FATEC 2019

# A probabilidade de que o ganhador de uma viagem entre artesãos brasileiros seja uma mulher de 65 anos ou mais.

# Resolução:
# Suponha que temos uma amostra de artesãos com diferentes idades e sexos.
# Sabemos que 9,24% dos artesãos são mulheres de 65 anos ou mais.

total_artesaos = 100  # Supondo um total de 100 artesãos (podemos ajustar para outros valores)
prob_mulheres_65_mais = 0.0924  # 9,24% de mulheres com 65 anos ou mais

# A probabilidade de que o ganhador seja uma mulher de 65 anos ou mais:
probabilidade = prob_mulheres_65_mais * total_artesaos

# Exibindo o resultado:
print(f"A probabilidade de o ganhador ser uma mulher de 65 anos ou mais é {probabilidade:.2f}%")

#Questão 10: EFOMM 2019

#Considere uma urna contendo 5 bolas brancas, 2 pretas e 3 verdes. Qual é a probabilidade de retirar três bolas da mesma cor?
# Cálculo das probabilidades
total_bolas = 5 + 2 + 3

# Probabilidade de retirar 3 bolas brancas
prob_brancas = comb(5, 3) / comb(total_bolas, 3)

# Probabilidade de retirar 3 bolas pretas (não é possível, pois só existem 2)
prob_pretas = 0

# Probabilidade de retirar 3 bolas verdes
prob_verdes = comb(3, 3) / comb(total_bolas, 3)

# Soma das probabilidades
probabilidade_total = prob_brancas + prob_verdes

# Exibindo o resultado
print(f"A probabilidade de retirar três bolas da mesma cor é {probabilidade_total * 100:.2f}%")

#Questão 11: UEPG 2018

#Em um grupo de 500 estudantes, 90 estudam Química, 160 estudam Biologia e 20 estudam ambas. Qual é a probabilidade de um aluno estudar Química ou Biologia?

# Dados fornecidos
total_estudantes = 500
estudam_quimica = 90
estudam_biologia = 160
estudam_ambas = 20

# Usamos a fórmula de probabilidade para união de dois conjuntos:
# P(A ou B) = P(A) + P(B) - P(A e B)
prob_quimica_ou_biologia = (estudam_quimica + estudam_biologia - estudam_ambas) / total_estudantes

# Exibindo o resultado
print(f"A probabilidade de um aluno estudar Química ou Biologia é {prob_quimica_ou_biologia:.2f}")

#Questão 12a: UNIFESP 2018

#Quantos grupos compostos por 2 alunos podem ser formados sem alunos fluentes em francês?

# Total de alunos fluentes apenas em inglês
fluentes_ingles = 6

# Combinação de 2 alunos fluentes apenas em inglês
grupos_sem_frances = comb(fluentes_ingles, 2)

# Exibindo o resultado
print(f"O número de grupos formados sem alunos fluentes em francês é {grupos_sem_frances}")

#Questão 12b: UNIFESP 2018

#Qual a probabilidade de, ao sortear dois alunos ao acaso, pelo menos um deles ser fluente em inglês?

# Dados fornecidos
total_alunos = 16
fluentes_ingles = 8  # Inclui alunos fluentes em inglês e inglês e francês

# Total de combinações possíveis de 2 alunos
total_combinacoes = comb(total_alunos, 2)

# Combinações de 2 alunos que não são fluentes em inglês
nao_fluentes_ingles = total_alunos - fluentes_ingles
combinacoes_nao_ingles = comb(nao_fluentes_ingles, 2)

# A probabilidade de pelo menos um ser fluente em inglês é o complementar
prob_pelo_menos_um_ingles = 1 - (combinacoes_nao_ingles / total_combinacoes)

# Exibindo o resultado
print(f"A probabilidade de pelo menos um dos alunos ser fluente em inglês é {prob_pelo_menos_um_ingles:.2f}")

#Questão 13: UERJ 2018

#Calcule a probabilidade de o jogador perder no jogo de memória.

# Probabilidade de acertar o primeiro par (temos 8 cartas e 2 iguais)
p_primeiro_acerto = 2 / 8

# Probabilidade de acertar o segundo par (6 cartas restantes e 2 iguais)
p_segundo_acerto = 2 / 6

# Probabilidade de acertar o terceiro par (4 cartas restantes e 2 iguais)
p_terceiro_acerto = 2 / 4

# Probabilidade de acertar o quarto par (2 cartas restantes e 2 iguais)
p_quarto_acerto = 2 / 2

# Probabilidade de ganhar
p_ganhar = p_primeiro_acerto * p_segundo_acerto * p_terceiro_acerto * p_quarto_acerto

# A probabilidade de perder é o complementar
p_perder = 1 - p_ganhar

# Exibindo o resultado
print(f"A probabilidade de perder o jogo é {p_perder:.2f}")

#Questão 14: ENEM PPL 2018

#Qual é a probabilidade de nascerem dois meninos e duas meninas?

from math import comb

# Probabilidade de menino ou menina em um nascimento
p_menino = 0.5
p_menina = 0.5

# Usamos o teorema binomial para calcular a probabilidade de 2 meninos e 2 meninas
p_nascer_2m_2f = comb(4, 2) * (p_menino ** 2) * (p_menina ** 2)

# Exibindo o resultado
print(f"A probabilidade de nascerem dois meninos e duas meninas é {p_nascer_2m_2f:.2f}")

#Questão 15: UFU 2018

#Qual é a probabilidade de as irmãs se sentarem uma ao lado da outra?

# Total de pessoas (duas irmãs e seus respectivos namorados)
total_pessoas = 4

# O número total de maneiras de dispor as pessoas no banco é 4! = 24
total_posicoes = 24

# Se considerarmos as irmãs como uma única unidade, temos 3! = 6 formas de dispor os casais.
# Cada casal pode trocar de lugar entre si (2! para as irmãs), então temos 2 * 6 = 12 maneiras.
posicoes_favoraveis = 12

# A probabilidade é a razão entre posições favoráveis e total
probabilidade = posicoes_favoraveis / total_posicoes

# Exibindo o resultado
print(f"A probabilidade de as irmãs sentarem-se uma ao lado da outra é {probabilidade:.2f}")

#Questão 16: PUCRJ 2018

#Qual é a probabilidade de sortear a letra "V" ou uma vogal de uma palavra com letras da palavra "VESTIBULAR"?

# Total de letras da palavra "VESTIBULAR"
total_letras = 10

# Letras específicas
vogais = "AEIOU"
letras_palavra = "VESTIBULAR"

# Probabilidade de tirar a letra "V"
p_v = letras_palavra.count('V') / total_letras

# Probabilidade de tirar uma vogal
p_vogal = sum([letras_palavra.count(letra) for letra in vogais]) / total_letras

# Exibindo os resultados
print(f"A probabilidade de tirar a letra V é {p_v:.2f}")
print(f"A probabilidade de tirar uma vogal é {p_vogal:.2f}")

#Questão 17: FGV 2018

#Qual é o total de bolas pretas em uma caixa se a probabilidade de sair uma bola preta duas vezes for 256/625?

# A fórmula da probabilidade de dois eventos independentes é (p/n)^2, onde p é o número de bolas pretas e n o total de bolas.
# Temos a seguinte equação: (p/n)^2 = 256/625

# Sabemos que a raiz quadrada de 256/625 é 16/25, logo p/n = 16/25, o que significa que há 16 bolas pretas de um total de 25.
total_bolas = 100
bolas_pretas = 16

# Calculamos a diferença entre as bolas pretas e brancas
diferenca = total_bolas - bolas_pretas

# Exibindo o resultado
print(f"O total de bolas pretas na caixa é {bolas_pretas}, e a diferença para as bolas brancas é {diferenca}.")

#Questão 18: UERJ 2018

#Um jogo consiste em lançar cinco vezes um dado cúbico. Um jogador é considerado vencedor se obtiver pelo menos três resultados pares. Qual é a probabilidade de vencer?

from math import comb

# Probabilidade de obter um número par em um dado
p_par = 3 / 6  # 1, 2, 3, 4, 5, 6, sendo 2, 4 e 6 pares
p_impar = 1 - p_par

# Precisamos calcular a probabilidade de obter 3, 4 ou 5 pares.
# Fórmula binomial: C(n, k) * (p^k) * (1-p)^(n-k)
n_lancamentos = 5

# Probabilidade de obter exatamente 3 pares
p_3_pares = comb(n_lancamentos, 3) * (p_par ** 3) * (p_impar ** 2)

# Probabilidade de obter exatamente 4 pares
p_4_pares = comb(n_lancamentos, 4) * (p_par ** 4) * (p_impar ** 1)

# Probabilidade de obter exatamente 5 pares
p_5_pares = comb(n_lancamentos, 5) * (p_par ** 5)

# Probabilidade total de vencer (somando as três possibilidades)
p_vitoria = p_3_pares + p_4_pares + p_5_pares

# Exibindo o resultado
print(f"A probabilidade de vencer é {p_vitoria:.2f}")

#Questão 19: Faculdade Albert Einstein - Medicina 2018

#Qual é a probabilidade de que o aluno escolhido aleatoriamente seja uma menina?

# Dados fornecidos
total_alunos_A = 24
total_meninas_A = 10
total_alunos_B = 30
total_meninas_B = 16

# Probabilidade de escolher uma menina
prob_menina_A = total_meninas_A / total_alunos_A
prob_menina_B = total_meninas_B / total_alunos_B

# A probabilidade total leva em conta a média ponderada
prob_total_menina = (prob_menina_A * total_alunos_A + prob_menina_B * total_alunos_B) / (total_alunos_A + total_alunos_B)

# Exibindo o resultado
print(f"A probabilidade de o aluno escolhido ser uma menina é {prob_total_menina:.2f}")

#Questão 20: UEMG 2018

#Um professor escolheu uma questão de Análise Combinatória aleatoriamente de dois tipos de prova. Sabendo que a questão escolhida foi de Análise Combinatória, qual é a probabilidade de a questão fazer parte da prova do tipo A?

# Dados fornecidos
questoes_AC_A = 3
questoes_AC_B = 6
total_questoes_A = 7
total_questoes_B = 8

# A probabilidade de ser uma questão de Análise Combinatória da prova A é a razão ponderada
prob_AC_A = questoes_AC_A / total_questoes_A
prob_AC_B = questoes_AC_B / total_questoes_B

# Usando a fórmula de probabilidade condicional:
p_A_dado_AC = (prob_AC_A * total_questoes_A) / ((prob_AC_A * total_questoes_A) + (prob_AC_B * total_questoes_B))

# Exibindo o resultado
print(f"A probabilidade de a questão ser da prova A é {p_A_dado_AC:.2f}")

#Questão 21: ENEM PPL 2018

#Qual a probabilidade de que um funcionário fumante seja do sexo feminino?

# Dados fornecidos
p_masculino = 0.70
p_feminino = 0.30
p_fumante_masculino = 0.05
p_fumante_feminino = 0.05

# Probabilidade de ser um fumante
p_fumante = (p_masculino * p_fumante_masculino) + (p_feminino * p_fumante_feminino)

# Probabilidade condicional de ser mulher dado que é fumante
p_mulher_dado_fumante = (p_feminino * p_fumante_feminino) / p_fumante

# Exibindo o resultado
print(f"A probabilidade de o funcionário fumante ser do sexo feminino é {p_mulher_dado_fumante:.2f}")

#Questão 22: UNESP 2018

#Dois dados convencionais foram lançados. Sabendo que saiu o número 6 em pelo menos um deles, qual é a probabilidade de que tenha saído o número 1 no outro?

# Total de combinações possíveis com dois dados
total_combinacoes = 6 * 6

# Casos favoráveis: o número 1 deve aparecer no dado que não é o 6
casos_favoraveis = 2  # (1, 6) e (6, 1)

# Casos possíveis com o número 6 aparecendo pelo menos uma vez
casos_com_6 = 11  # (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6)

# A probabilidade é a razão entre os casos favoráveis e os casos possíveis com o número 6
probabilidade = casos_favoraveis / casos_com_6

# Exibindo o resultado
print(f"A probabilidade de que o número 1 tenha saído no outro dado é {probabilidade:.2f}")




