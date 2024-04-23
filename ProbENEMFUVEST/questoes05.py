# Capítulo 5 - ENEMs - Vestibulares da Fuvest - 25 questões resolvidas

from math import comb
# 01) Uma caixa contém 20 peças em boas condições e 15 em más condições.
# Uma amostra de 10 peças é extraída. Calcular a probabilidade de que ao
# menos uma peça na amostra seja defeituosa

# Pelo menos uma peça defeituosa = 1 - nenhuma peça defeituosa
# nenhuma peça defeituosa = comb(15, 10) / comb(35, 10)
# 1 - comb(15, 10) / comb(35, 10)
# = 19/18879 = 0.001
x = 1 - 0.001
print(x) # 0.999946

# 02) (Pôquer com dados) Cinco dados são jogados simultaneamete e os resultados são classificados em:
# Ai = todos diferentes;
# A2 = um par;
# A3 = dois pares;
# 44 = três iguais;
# /I5 = full (três iguais e dois iguais);
# A6 = quatro iguais (pôquer);
# 47 = cinco iguais;
# A& = uma sequência.
# Calcular as probabilidades de A, i — 1,2,9.

# A1 = todos diferentes = 6! / 6^5
# A2 = um par = C(5-2) * 6 * 5 * 4 * 3 / 6^5
# A3 = dois pares = C(6-2)* C(5,2)* C(3,2) * 4 / 6^5
a1 = 720 / 7776
a2 = 3600 / 7776
a3 = 1800 / 7776
print(a1, a2, a3) # 0.0926 0.4629 0.2314

# 03) Uma cidade tem 30 000 habitantes e trêsjornais A, B e C. Uma pesquisa
#de opinião revela que:
#12 000 leem A\
#8 000 leem B;
#7 000 leem A e B;
#6 000 leem C;
#4 500 leem A e C;
#1 000 leem B e C;
#500 leem A, B e C.
#Qual é a probabilidade de que um habitante leia
#(a) pelo menos um jornal?
#(b) somente um jornal?

# a) Temos que usar teoria dos conjuntos para facilitar.
#lógica é subtrair as intersecções para encontrar a parte dos conjuntos incomum aos outros.
# Pelo menos um jornal = A U B U C = A + B + C - A ∩ B - A ∩ C - B ∩ C + A ∩ B ∩ C
# A = 12000, B = 8000, C = 6000
# A ∩ B = 7000, A ∩ C = 4500, B ∩ C = 1000
# A ∩ B ∩ C = 500
# A U B U C = 12000 + 8000 + 6000 - 7000 - 4500 - 1000 + 500
# = 20500
# Pelo menos um jornal = 20500 / 30000
# = 0.6833
x = 20500 / 30000
print(x) # 0.6833


# b) Somente um jornal = A - A ∩ B - A ∩ C + A ∩ B ∩ C
# = 12000 - 7000 - 4500 + 500
# = 5000
# Somente um jornal = 5000 / 30000
# = 0.1667

x = 5000 / 30000
print(x) # 0.1667



# 04 ) Em uma sala de aula com 20 alunos, há apenas 4 alunos que nunca foram
#reprovados. Selecionando aleatoriamente dois estudantes desta sala, qual a
#probabilidade de que smbos nunca tenham sido reprovados.
# P(a) = C(4-2) / C(20-2)
x = comb(4, 2) / comb(20, 2)
print (6/190)

# 05) Se lançarmos um dado, qual a probabilidade de obtermos um número maior que 4? 
# P = 2/6 = 1/3 = 0.3333
x = 2/6
print(x) # 0.3333

# 06) Um restaurante está com 13 pessoas: 9 clientes e 4 garçons. Se escolhermos uma pessoa do local aleatoriamente, qual a probabilidade de ser um cliente?
# P = 9/13 = 0.6923
x = 9/13
print(x) # 0.6923

# 07) João possui um pote com balas coloridas. Ele resolveu contar quantas balas de cada cor havia no recipiente e chegou aos números:
#6 balas vermelhas
#3 balas verdes
#5 balas brancas
#7 balas amarelas
#Colocando todas as balas de volta ao pote e escolhendo dois doces para comer, qual a probabilidade de João pegar aleatoriamente uma bala vermelha 
#e uma amarela em sequência, sem repor a primeira retirada?

# P = (6/21) * (7/20) = 0.1
x = (6/21) * (7/20)
print(x) # 0.1

# 08) Se lançarmos dois dados ao mesmo tempo, qual a probabilidade de dois números iguais ficarem voltados para cima?
# P = 6/36 = 1/6 = 0.1667
x = 6/36
print(x) # 0.1667

#09) Uma pesquisa realizada com 800 pessoas sobre a preferência pelos telejornais de uma cidade, evidenciou que 200 entrevistados assistem 
#o apenas o telejornal A, 250 apenas o telejornal B e 50 assistem A e B. 
#Das pessoas entrevistadas, qual a probabilidade de sortear ao acaso uma pessoa que assiste o telejornal A ou o telejornal B?

# P = (200 + 250 - 50) / 800 = 0.625
x = (200 + 250 - 50) / 800
print(x) # 0.625

# 10) O diretor de uma escola convidou os 280 alunos de terceiro ano a participarem de uma brincadeira. Suponha que existem 5 objetos e 6 personagens numa casa de 9 cômodos; um dos personagens esconde um dos objetos em um dos cômodos da casa.
#O objetivo da brincadeira é adivinhar qual objeto foi escondido por qual personagem e em qual cômodo da casa o objeto foi escondido. Todos os alunos decidiram participar. A cada vez um aluno é sorteado e dá a sua resposta.
#As respostas devem ser sempre distintas das anteriores, e um mesmo aluno não pode ser sorteado mais de uma vez. Se a resposta do aluno estiver correta, ele é declarado vencedor e a brincadeira é encerrada.
#O diretor sabe que algum aluno acertará a resposta porque há:

# 5*6*9 = 270 
# 280 - 270 = 10
print(10)

# 11) Em um jogo há duas urnas com dez bolas de mesmo tamanho em cada urna. A tabela a seguir indica as quantidades de bolas de cada cor em cada urna
# urna 1: 0 bolas vermelhas, 3 bolas azuis, 1 bolas verdes, 4 bolas amarelas e 2 bolas brancas
# urna 2: 4 bolas vermelhas, 1 bolas azuis, 3 bolas verdes, 0 bolas amarelas e 2 bolas brancas
# Se uma bola for retirada de cada urna, qual a probabilidade de que ambas sejam azuis?
#P(A) = 3/10
#P(B) = 1/10
#P(A ∩ B) = 3/10 * 1/10 = 3/100
print(3/100)

# 12) Numa escola com 1.200 alunos foi realizada uma pesquisa sobre o conhecimento desses em duas línguas estrangeiras: inglês e espanhol.
# Nessa pesquisa constatou-se que 600 alunos falam inglês, 500 falam espanhol e 300 não falam qualquer um desses idiomas.
# Escolhendo-se um aluno dessa escola ao acaso e sabendo-se que ele não fala inglês, qual a probabilidade de que esse aluno fale espanhol?
# Fala pelo menos uma língua = 1200 - 300 = 900
# Falam inglês e espanhol = 600 + 500 - 900 = 200
# 1200 - 600 = 600
# 500 - 200 = 300
# 300 / 600 = 0.5
print(1/2)

# 13) Numa sala existem duas caixas com bolas amarelas e verdes. Na caixa 1, há 3 bolas amarelas e 7 bolas verdes. Na caixa 2, há 5 bolas amarelas e 5 bolas verdes. De forma aleatória, uma bola é extraída da caixa 1, 
# sem que se saiba a sua cor, e é colocada na caixa 2. Após esse procedimento, a probabilidade de extrair uma bola amarela da caixa 2 é igual a
# P(amarela e amarela) = 3/10 * 6/11 = 18/110 = 9/55
# P(verde e amarela) = 7/10 * 5/11 = 35/110 = 7/22
# P(amarela) = 9/55 + 7/22 = 53/110
print(53/110)

# 14) Um kit para impressão vem com oito cartuchos de tinta, de formato idêntico, para impressora. Nesse kit há dois cartuchos de cada uma das quatro cores diferentes necessárias para uma impressora caseira (ciano, magenta, amarelo e preto). 
# Escolhendo aleatoriamente dois cartuchos desse kit, qual a probabilidade de se obter duas cores distintas?
# P = 1 - 1/7
print(6/7)

# 15) Uma urna contém 5 bolas brancas e 3 bolas pretas. Três bolas são retiradas ao acaso, sucessivamente, sem reposição. Determine:
#A) A probabilidade de que tenham sido retiradas 2 bolas pretas e 1 bola branca.
#B) A probabilidade de que tenham sido retiradas 2 bolas pretas e 1 bola branca, sabendo-se que as três bolas não são da mesma cor.
# P(A) = 3/8 * 2/7 * 5/6 = 5/56
# P(B) = 3/8 * 2/7 * 5/6 / 5/56 = 5/12

print(5/56)
print(5/12)

# 16) Em uma empresa, os funcionários podem ter plano de saúde ou não. Sabe-se que 70% dos funcionários têm plano de saúde e 30% não têm. A probabilidade de um funcionário, escolhido ao acaso, estar satisfeito com o plano de saúde, 
# dado que ele o tem, é de 0,9. Se um funcionário é escolhido ao acaso e informa estar satisfeito com o plano de saúde, a probabilidade de ele ter plano de saúde é:
#P(a) = 0.70
#P(b) = 0.90
# Seja A o evento "ter plano de saúde" e B o evento "estar satisfeito com o plano de saúde". Queremos calcular a probabilidade de A dado B, ou seja, P(A|B).
#P(A) = 0,70
#P(B|A) = 0,90
#P(A|B) = P(A ∩ B) / P(B) = P(B|A) * P(A) / P(B)
#P(B) = P(B|A) * P(A) + P(B|A') * P(A')
#P(B) = 0,90 * 0,70 + 0,10 * 0,30 = 0,63 + 0,03 = 0,66
# P(A|B) = (0,90 * 0,70) / 0,66 ≈ 0,952
print(0.952)

# 17) (Enem 2015) Em uma central de atendimento, cem pessoas receberam senhas numeradas de 1 até 100. Uma das senhas é sorteada ao acaso.
#Qual a probabilidade de a senha sorteada ser um número de 1 a 20?

# P = 20/100 = 0.2
print(0.2)

#18) Em uma reserva florestal existem 263 espécies de peixes, 122 espécies de mamíferos, 93 espécies de répteis, 1 132 espécies de borboletas e 656 espécies de
#aves. Se uma espécie animal for capturada ao acaso, qual a probabilidade de ser uma borboleta?

# P = 1132 / (263 + 122 + 93 + 1132 + 656) = 0.41
print(0.41)

# 19) Um programa de televisão criou um perfil em uma rede social, e a ideia era de que esse perfil fosse sorteado para um dos seguidores, quando esses fossem em número de um milhão. Agora que essa quantidade de seguidores foi atingida, os organizadores perceberam que apenas 80% deles são realmente fãs do programa. Por conta disso, resolveram que todos os seguidores farão um teste, com perguntas objetivas referentes ao programa, e só poderão participar do sorteio aqueles que forem aprovados. 
# Estatísticas revelam que, num teste dessa natureza, a taxa de aprovação é de 90% dos fãs e de 15% dos que não são fãs.
# De acordo com essas informações, a razão entre a probabilidade de que um fã seja sorteado e a probabilidade de que o 
# sorteado seja alguém que não é fã do programa é igual a

# 800.000 sao fãs e 200.000 não são fãs
# 90% dos fãs = 720.000
# 15% dos não fãs = 30.000
# P(a) = 720.000 / 750.000 = 0.96
# P(b) = 30.000 / 750.000 =  0.04
x = 720000 / 30000
print(x)

# 20) Um morador de uma região metropolitana tem 50% de probabilidade de atrasar-se para o trabalho quando chove na região; 
# caso não chova, sua probabilidade de atraso é de 25%. Para um determinado dia, o serviço de meteorologia estima em 30% a probabilidade da ocorrência de chuva nessa região.
# Qual é a probabilidade de esse morador se atrasar para o serviço no dia para o qual foi dada a estimativa de chuva?

# chova e atrase : 30% * 50% = 15%
# não chova e atrase : 70% * 25% = 17.5%
# P = 15% + 17.5% = 32.5%
print(32.5)

# 21) Uma aluna estuda numa turma de 40 alunos. Em um dia, essa turma foi dividida em três salas, A, B e C, de acordo com a capacidade das salas. 
# Na sala A ficaram 10 alunos, na B, outros 12 alunos e na C, 18 alunos. Será feito um sorteio no qual, primeiro, será sorteada uma sala e, 
# posteriormente, será sorteado um aluno dessa sala.
# Qual é a probabilidade de aquela aluna específica ser sorteada, sabendo que ela está na sala C

# P(a) = 1/3 * 1/18 = 1/54
print(1/54)

# 22) Um apostador deve escolher uma entre cinco moedas ao acaso e lançá-la sobre uma mesa, tentando acertar qual resultado (cara ou coroa) sairá na face superior da moeda.
# Suponha que as cinco moedas que ele pode escolher sejam diferentes:
# • duas delas têm “cara” nas duas faces;
# • uma delas tem “coroa” nas duas faces;
# • duas delas são normais (cara em uma face e coroa na outra).
# Nesse jogo, qual é a probabilidade de o apostador obter uma face “cara” no lado superior da moeda lançada por ele?

# escolha moeda com duas caras : 2/5 * 100% = 40%
# uma moeda so com coroa : 1/5 * 0% = 0%
# escolha moeda normal : 2/5 * 50% = 20%
print(60/100)

# 23) O dono de um restaurante situado às margens de uma rodovia percebeu que, ao colocar uma placa de propaganda de seu restaurante ao longo da rodovia, as vendas 
# aumentaram. Pesquisou junto aos seus clientes e concluiu que a probabilidade de um motorista perceber uma placa de anúncio é 1/2. Com isso, após autorização do 
# órgão competente, decidiu instalar novas placas com anúncios de seu restaurante ao longo dessa rodovia, de maneira que a probabilidade de um motorista perceber 
# pelo menos uma das placas instaladas fosse superior a 99/100. A quantidade mínima de novas placas de propaganda a serem instaladas é

# 1 placa = 50%
# 2 placas = 75%
# 3 placas = 87.5%
# 4 placas = 93.75%
# 5 placas = 96.875%
# 6 placas = 98.4375%
# 7 placas = 99.21875%

print(7)

# 24) organizador de uma competição de lançamento de dardos pretende tornar o campeonato mais competitivo. Pelas regras atuais da competição, numa rodada, 
# o jogador lança 3 dardos e pontua caso acerte pelo menos um deles no alvo. O organizador considera que, em média, os jogadores têm, em cada lançamento, 1/2 
# de probabilidade de acertar um dardo no alvo.
# A fim de tornar o jogo mais atrativo, planeja modificar as regras de modo que a probabilidade de um jogador pontuar em uma rodada seja igual ou superior a 9/10. 
# Para isso, decide aumentar a quantidade de dardos a serem lançados em cada rodada.
# Com base nos valores considerados pelo organizados da competição, a quantidade mínima de dardos que devem ser disponibilizados em uma rodada 
# para tornar o jogo mais atrativo é:

# 1 dardo = 50%
# 2 dardos = 75%
# 3 dardos = 87.5%
# 4 dardos = 93.75%

print(4)

# 25) Amigo secreto é uma brincadeira tradicional nas festas de fim de ano. Um grupo de amigos se reúne e cada um deles sorteia o nome da pessoa que irá presentear. 
# No dia da troca de presentes, uma primeira pessoa presenteia seu amigo secreto. Em seguida, o presenteado revela seu amigo secreto e o presenteia. 
# A brincadeira continua até que todos sejam presenteados, mesmo no caso em que o ciclo se fecha. Dez funcionários de uma empresa, entre eles um casal, 
# participarão de um amigo secreto. A primeira pessoa a revelar será definida por sorteio.
# Qual é a probabilidade de que a primeira pessoa a revelar o seu amigo secreto e a última presenteada sejam as duas pessoas do casal?

# p(a) = 8!*2/10! = 1/45
print(1/45)


















