# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo C�rtes Nogueira da Rocha Pita

#Ex. 1
print "Hello world!"

#DRE: 117093691
#Rodrigo C�rtes Nogueira da Rocha Pita

#Ex. 2
print ""
print ""

DRE = input("Digite o n�mero do aluno:")
P1 = input("Digite a nota da P1:")
P2 = input("Digite a nota da P2:")
MT = input("Digite a m�dia dos testes:")

media = (P1 + P2)/2 * 0.8 + MT * 0.2

print "Aluno:", DRE
print "Notas:", P1, P2, MT
print "M�dia:", media

#DRE: 117093691
#Rodrigo C�rtes Nogueira da Rocha Pita

#Ex. 3
print ""
print ""
print "Resolvendo equa��o do segundo grau"
print ""
import math

a, b, c = input("Digite os valores dos coeficientes num�ricos a, b, c:")

delta = b*b - 4*a*c

if delta < 0:
    print "A equa��o n�o apresenta raizes reais"
    
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print "As raizes s�o:", x1, "e", x2

    else:
        x = (-b - math.sqrt(delta))/(2*a)
        print "A raiz �:", x

#DRE: 117093691
#Rodrigo C�rtes Nogueira da Rocha Pita

#Ex. 4
print ""
print ""
print "Calculando a �rea de um tri�ngulo"
print ""
import math

a, b, c = input("Insira os valores dos lados a, b, c:")

s = (a+b+c)/2

if a+b > c and a+c > b and b+c > a:
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print "A �rea do tri�ngulo �:", A
    if a == b == c:
        print "O tri�ngulo � equil�tero"
    elif a == b != c or a == c != b or b == c != a:
        print "O tri�ngulo � is�sceles"
    else:
        print "O tri�ngulo � escaleno"
else:
    print "O tri�ngulo n�o existe"
    
print ""
print ""

print "Good bye, world!"




