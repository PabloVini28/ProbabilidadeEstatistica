# Morgado 2.4 - Questões - 5 questões resolvidas

# 01)  De quantos modos 5 meninos e 5 meninas podem formar uma roda de
# ciranda de modo que pessoas de mesmo sexo não fiquem juntas?
# p (5-1)! = 4! meninos
# p'(5-1)! = 4! meninas
x = 24*24
print(x)

# 03)  De quantos modos n casais podem formar uma roda de ciranda de modo
# que cada homem permaneça ao lado de sua mulher?

# (n-1)! modos de se por os casais
# 2^n modos de se por os casais - direita ou esquerda
# 2^n * (n-1)!
x = 2**3 * 2
print(x)

# 07)  De quantos modos 5 mulheres e 6 homens podem formar uma roda de
# ciranda de modo que as mulheres permaneçam juntas?

# se as mulheres ficam em grupo, logo 1 grupo + 6 homens = 7!
# (n-1)! = (7-1)! = 6!
# 6! * 5! = 720 * 120 = 86400 - permutação simples entre as mulheres em 5!
x = 720*120
print(x)

# 05) São dados n pontos em um círculo. Quantos zr-ágonos (não necessariamente convexos) existem com vértices nesses pontos?
def num_zragonos(n):
    if n < 3:
        return 0
    else:
        return ((n - 1) * (n - 3)) // 4

n = 5
resultado = num_zragonos(n)
print(resultado)

# 06) Uma pulseira deve ser cravejada com um rubi, uma esmeralda, um topázio, uma água-marinha, uma turmalina e uma ametista. De quantos modos
# isso pode ser feito supondo:
# a) que a pulseira tem fecho e um relógio engastado no fecho;
x = 6*5*4*3*2*1
print(x)
# b) que a pulseira tem fecho;
x = 6*5*4*3*2 / 2
print(x)
# c) que a pulseira não tem fecho e o braço só pode entrar na pulseira em
# um sentido;
#5! - sem fecho, a pulseira pode rodar no braço 
x = 5*4*3*2*1
print(x)
# d) que a pulseira não tem fecho e o braço pode entrar na pulseira nos
# dois sentidos
# a pulseira pode rodar no braço e o braço pode entrar em dois sentidos
x = 5*4*3*2*1 / 2
print(x)


