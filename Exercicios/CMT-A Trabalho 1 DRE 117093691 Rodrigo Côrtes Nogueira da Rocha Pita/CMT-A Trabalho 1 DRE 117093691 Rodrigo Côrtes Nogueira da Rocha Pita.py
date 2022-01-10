# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 1
print "Hello world!"

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 2
print ""
print ""

DRE = input("Digite o número do aluno:")
P1 = input("Digite a nota da P1:")
P2 = input("Digite a nota da P2:")
MT = input("Digite a média dos testes:")

media = (P1 + P2)/2 * 0.8 + MT * 0.2

print "Aluno:", DRE
print "Notas:", P1, P2, MT
print "Média:", media

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 3
print ""
print ""
print "Resolvendo equação do segundo grau"
print ""
import math

a, b, c = input("Digite os valores dos coeficientes numéricos a, b, c:")

delta = b*b - 4*a*c

if delta < 0:
    print "A equação não apresenta raizes reais"
    
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print "As raizes são:", x1, "e", x2

    else:
        x = (-b - math.sqrt(delta))/(2*a)
        print "A raiz é:", x

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 4
print ""
print ""
print "Calculando a área de um triângulo"
print ""
import math

a, b, c = input("Insira os valores dos lados a, b, c:")

s = (a+b+c)/2

if a+b > c and a+c > b and b+c > a:
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print "A área do triângulo é:", A
    if a == b == c:
        print "O triângulo é equilátero"
    elif a == b != c or a == c != b or b == c != a:
        print "O triângulo é isósceles"
    else:
        print "O triângulo é escaleno"
else:
    print "O triângulo não existe"
    
print ""
print ""

print "Good bye, world!"




