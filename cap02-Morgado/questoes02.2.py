# Morgado 2.2 - Questões - 12 questões resolvidas

# 01) Quantos são os anagramas da palavra CAPÍTULO 
# a) começam com consoante e terminam com vogal
x = 4*4*6*5*4*3*2
print(x)

# 02) . Permutam-se de todos os modos possíveis os algarismos 1,2,4,6,7 e
# escrevem-se os números assim formados em ordem crescente.
# a) que lugar ocupa o número 62417?
x = 5*4*3*2*1
print(x)

# 03)  De quantos modos é possível sentar 7 pessoas em cadeiras em fila de
# modo que duas determinadas pessoas dessas 7 não fiquem juntas?

x = 7*6*5*4*3*2*1
# AB ou BA não podem ficar juntos
y = 2*(6*5*4*3*2)
print(x-y)

# 05)  quantos modos é possível colocar em uma prateleira 5 livros de matemática, 3 de física e 2 de estatística, de modo que os livros de um mesmo
# assunto permaneçam juntos?
# ordem dos livros 3*2*1
# ordem de apresentação 5! * 3! * 2!
x = 5*4*3*2*1 * 3*2*1 * 2*1 * 3*2*1
print(x)

# 06)  Quantas são as permutações dos números (1,2,..., 10) nas quais o 5 está
# situado à direita do 2 e à esquerda do 3, embora não necessariamente em
# lugares consecutivos?
# 10!/3! = 604800
x = 604800
print(x)

# 07)  De quantos modos podemos dividir 12 pessoas: 
# a)  em dois grupos de 6?
x = 12*11*10*9*8*7/(6*5*4*3*2*1)
print(x)

# 08) De quantos modos r rapazes e m moças podem se colocar em fila de
# modo que as moças fiquem juntas?

# (r+1)
# m!(r+1)

# 09) Delegados de 10 países devem se sentar em 10 cadeiras em fila. De
# quantos modos isso pode ser feito se os delegados do Brasil e de Portugal
# devem se sentar juntos e o do Iraque e o dos Estados Unidos não podem
# sentar juntos?

# Brasil e Portugal
# 2 * 9! = 725760

# Iraque e Estados Unidos
# 2*2*8! = 161280

x = 725760 - 161280
print(x)

# 10) Um cubo de madeira tem uma face de cada cor. Quantos dados diferentes podemos formar gravando números de 1 a 6 sobre essas faces?
x = 6*5*4*3*2*1
print(x)

# 11) Quantos dados diferentes podemos formar gravando números de 1 a 6
# sobre as faces indistinguíveis de um cubo de madeira?

x = 720 /24 # 24 é o número de permutações de 6 elementos para serem gravadas numa face do cubo
print(x)

# 12)   Resolva o problema anterior para:
# a) números de 1 a 4, tetraedro regular;
x = 4*3*2/12 # 12 é o número de permutações de 4 elementos para serem gravadas numa face do tetraedro
print(x)

# 13) Um campeonato é disputado por 12 clubes em rodadas de 6 jogos cada.
# De quantos modos é possível selecionar os jogos de primeira rodada?

x = 11*9*7*5*3*1 # Possíves adversários para o primeiro time
print(x)





