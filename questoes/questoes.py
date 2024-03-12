
# QUESTÕES REFERENTES À DISCIPLINA DE PROBABILIDADE E ESTATÍSTICA ; TURMA 2024.1
# DISCENTES: PABLO VINICIOS DA SILVA ARAÚJO E RAUL RONALD DINIZ MARINHO;
# DOCENTE: ANTÔNIO JOEL RAMIRO DE CASTRO;
# LIVRO ADOTADO: ANALISE COMBINATÓRIA E PROBABILIDADE - MORGADO;

#CAP 02 -

# QUESTÃO 1
#Quantas palavras contendo 3 letras diferentes podem ser for-
#madas com um alfabeto de 26 letras

def function():
    n = 26
    resultado = n * (n-1) * (n-2)
    print(resultado)

# QUESTÃO 2
#Quantos são os gabaritos possíveis 10 questões
#de múltipla-escolha, com cinco a1ternativas por questão?

def function2():
    n = 5
    resultado = n ** 10
    print(resultado)

# QUESTÃO 3
#Quantos inteiros há entre 1000 e 9999 cujos algarismos são
#distintos?  

def function3():
    n = 9 * 9 * 8 * 7
    print(n)   

# QUESTÃO 4
#De quantos modos diferentes podem ser escolhidos um presi-
#dente e um secretario de um conselho que tem 12 membros?  

def function4():
    n = 12 * 11
    print(n)      

# QUESTÃO 5
#De quantos modos 3 pessoas podem sentar-se em 5 cadeiras em fila?

def function5():
    n = 5 * 4 * 3
    print(n)

# QUESTÃO 6
#Quantos numeros de quatro dígitos são maiores que 2400 e
# a) tem todos os digitos diferentes?
def function6a():
    #indo de 2400 a 3000
    n1 =  1*8*7*6
    #indo de 3000 a 9999
    n2 =  7*9*8*7
    x = n1 + n2
    print(x)

# b) não tem digitos iguais a 3,5 ou 6


# QUESTÃO 8
# Quantos divisores naturais possuem o número 360? Quantos
# são pares?
    
def function8():
    n = 360
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
    print(cont)    

# QUESTÃO 9
#Quantos são os números naturais de 4 dígitos que possuem
#pelo menos dois dígitos iguais
def function9():
    n = 9*10*10*10
    m = 9*8*7*6
    print(n-m)

#QUESTÃO 11
#De quantos modos podemos arrumar 8 torres iguais em um
#tabuleiro de xadrez (8 x 8) (de modo que não haja duas torres na
#mesma linha nem na mesma coluna?
def function11():
    n = 64*49*36*25*16*9*4*1
    print(n)
    
    

def main():
    function()
    function2()
    function3()
    function4()
    function5()
    function6a()
    function8()
    function9()
    function11()


if __name__ == "__main__":
    main()

