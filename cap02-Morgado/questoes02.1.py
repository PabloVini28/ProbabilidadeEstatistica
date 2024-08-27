# Morgado 2.1 - Questões - 4 questões resolvidas


# 7. O conjunto A possui 4 elementos e o conjunto B possui 7 elementos.
# Quantas são as funções f: A → B? Quantas são as funções injetoras f: A → B?

x = 7 ** 4

print (x)

x = 7 * 6 * 5 * 4

print (x)


# 10. Quantos subconjuntos possui um conjunto que tem n elementos?

print ('2 elevado a n')

# 26. a) Quantas são as palavras de 5 letras distintas de um alfabeto de 26 letras nas quais a letra A figura mas não é a letra inicial da palavra?
letras_restantes = 25  # Letras restantes depois de fixar a letra A
posicoes = 4  # Posições restantes onde a letra A pode estar
x = letras_restantes * letras_restantes * letras_restantes * letras_restantes * posicoes
print(x)  # Resposta para a): 1214400

# b) Refaça o item a) suprimindo a palavra distintas do enunciado.
x = 26 ** 5 - 26 ** 4
print(x)  # Resposta para b): 1658775

