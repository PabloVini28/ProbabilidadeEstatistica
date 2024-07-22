print("=================================================================")
print("|  Morgado 3.3 (Os Lemas de Kaplansky) - 8 questões resolvidas  |")
print("=================================================================", "\n")

print("01) 5 pessoas devem se sentar em 15 cadeiras colocadas em tomo de uma mesa circular.")
print("De quantos modos isso pode ser feito se não deve haver ocupação simultânea de duas")
print("cadeiras adjacentes?", "\n")

# O número de modos de escolher as cadeiras que serão usadas é g(15,5) = 378. Escolhidos
# as cadeiras, há 5! = 120 modos de designá-las para as 5 pessoas.
# A resposta é 378 x 120 = 45.360.
n_modos_total = 378
n_modos_escolher = 120
result = n_modos_total * n_modos_escolher
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("02) Dado um decágono, quantos são os triângulos cujos vértices são vértices")
print("não consecutivos do decágono?", "\n")

# Para formar um triângulo, devemos escolher três vértices não consecutivos.

# Para formar um triângulo, devemos escolher três vértices não consecutivos.
# Total de triângulos possíveis
total_triangulos = 120

# Triângulos com vértices consecutivos
triangulos_consecutivos = 10 * 7

# Triângulos não consecutivos
triangulos_nao_consecutivos = total_triangulos - triangulos_consecutivos

result = triangulos_nao_consecutivos
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("03) De quantos modos podemos formar uma sequência de p elementos iguais a 1 e")
print("q elementos iguais a 0 se dois elementos iguais a zero não podem ser adjacentes?", "\n")

# Devemos escolher q posições, sem que sejam escolhidas duas posições consecutivas,
# dentre as p + q posições da sequência para pôr os zeros; feito isto, as posições
# restantes serão ocupadas pelos 1.

print("Resposta: f(p+q,q)  =  C_(p+1)^q  =  (p+1)! / q!(p-q+1)!  modos.", "\n")


print("--------------------------------------------------------------", "\n")


print("04) De quantos modos podemos formar uma sequência de p elementos iguais a 2,")
print("q elementos iguais a 1 e r elementos iguais a 0 se dois elementos iguais a")
print("zero não podem ser adjacentes?", "\n")

# Devemos escolher r posições, sem que sejam escolhidas duas posições consecutivas,
# dentre as p + q + r posições da sequência para pôr os zeros; isso pode ser feito
# de f(p + q + r, r) = C_((p+q+r)-r+1)^r.

print("Resposta: C_(p+q+1)^r * C_(p+q)^p  modos.", "\n")


print("--------------------------------------------------------------", "\n")


print("05) De quantos modos é possível formar uma roda de ciranda com 7 meninas e")
print("12 meninos sem que haja duas meninas em posições adjacentes?", "\n")

# Devemos escolher 7 dos 19 lugares da roda para pôr as meninas, o que pode ser feito
# de g(19,7) = 19/12 * C_12^7 modos.

# Em seguida, devemos pôr as 7 meninas nos 7 lugares selecionados, o que pode ser feito
# de 7! modos, e os 12 meninos nos 12 lugares restantes, o que pode ser feito de 12!
# modos. Como a roda pode ser girada de 19 modos, contamos cada roda 19 vezes.

print("Resposta: (11!)^2 / 10  ≅  1,6 * 10^14 .", "\n")


print("--------------------------------------------------------------", "\n")


print("06) Quantos são os anagramas de araraquara que não possuem duas letras a consecutivas?", "\n")

# Das 10 posições do anagrama, devemos escolher 5, sem que sejam escolhidas duas posições
# adjacentes, para pôr as letras A, o que pode ser feito de f(10,5) = 6 modos.

# Em seguida, devemos escolher 3 das 5 posições restantes para pôr os R, o que pode ser
# feito de 10 modos. Finalmente, devemos pôr as letras U e Q nas duas posições restantes,
# o que pode ser feito de 2 modos. Então a resposta será 6 x 10 x 2 = 120.

result = 6 * 10 * 2
print("Resposta:", result, "\n")


print("--------------------------------------------------------------", "\n")


print("07) De quantos modos é possível formar um p-subconjunto de {1,2,...,n} de modo")
print("que entre cada dois elementos escolhidos para o subconjunto haja, no conjunto,")
print("pelo menos r elementos não escolhidos para o subconjunto?", "\n")

# Marcando o sinal + os elementos selecionados e com o sinal — os elementos não selecionados,
# devemos arrumar em fila p sinais + e n — p sinais — de modo que entre dois sinais + haja,
# pelo menos, r sinais —. Inicialmente vamos formar uma fila apenas com os sinais +.
# Os sinais — serão colocados nos p + 1 espaços existentes entre os sinais +, antes do
# primeiro e depois do último. Para decidir quantos sinais — serão colocados em cada um
# desses espaços, devemos resolver, em números inteiros, a equação x1 + x2 +...+ x_p+1 = n - p,

# Fazendo x2 = r + y2, ..., x_p = r + y_p, a equação transforma-se em
# x1 + y2 +...+ y_p + x_(p+1) + (p — 1)r = n - p  , ou seja,
# x1 + y2 +...+ y_p + x_(p+1) = n — p — (p — 1)r  ,
# com todas as incógnitas inteiras e não negativas.

print("Resposta: f(n,p,r)  =  C_(n-(p-1)r)^p  modos.", "\n")


print("--------------------------------------------------------------", "\n")


print("08) Refaça o problema anterior no caso circular. Nesse caso, por exemplo, tomando")
print("n = 6, o conjunto {1,2,3,4,5,6} é tal que entre 1 e 4 há dois elementos, entre")
print("5 e 1 há um elemento, entre 6 e 4 há três elementos.", "\n")

# Vamos contar separadamente os subconjuntos, conforme contenham ou não algum dos
# elementos 1, 2, ..., r.
# O número de subconjuntos que não contêm nenhum desses elementos é f(n - r , p, r).
# O número de subconjuntos que contêm um desses elementos é r * f(n-2r-1 , p-1,r).
# Então, o total de subconjuntos será: f(n - r , p, r)  +   r * f(n-2r-1 , p-1,r)

print("Resposta: g(n,p,r)  =  n / (n-pr) *  C_(n-pr)^p", "\n")


print("--------------------------------------------------------------", "\n")