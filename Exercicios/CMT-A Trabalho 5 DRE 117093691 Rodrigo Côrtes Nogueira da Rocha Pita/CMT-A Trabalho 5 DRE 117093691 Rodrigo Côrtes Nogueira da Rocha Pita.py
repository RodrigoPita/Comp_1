     # -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 1
S = 0
print "Calculando o Somatório:"
print
for x in range(1, 1000000):
    S += 1.0/(x) ** 2
print S
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 2
import math
print "Aproximação de pi:"
print
S1 = 0
S2 = 0
for x in range(1, 11, 2):
    S1 += 1.0/(x) ** 2
for y in range(2, 11, 2):
    S2 += 1.0/(y) ** 2
pi = math.sqrt(12 * (S1 - S2))
print pi
print
print "-" * 40
print

#Desafio 2.1
import math
print "Aproximação de pi:"
print
S1 = 0
S2 = 0
z = input("Escolha o número de termos: ")
for x in range(1, (z + 1), 2):
    S1 += 1.0/(x) ** 2
for y in range(2, (z + 1), 2):
    S2 += 1.0/(y) ** 2
pi = math.sqrt(12 * (S1 - S2))
print pi
print 
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 3
print "Tabuadas:"
print
for x in range(3, 21):
    print "Tabuada do", x
    for k in range(1, 11):
        print x, "x", k, "=", x*k
    print
print
print "-" * 40
print

#Desafio 3.1
import locale
print "Tabuadas(alinhadas):"
print
for x in range(3, 21):
    print "Tabuada do", x
    for k in range(1, 11):
        print locale.format('%d', x), "x", locale.format('%2d', k), "=", locale.format('%3d', (x * k))
    print
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 4
print "Números de Armstrong:"
print
for c in range(0, 10):
    for d in range(0, 10):
        for u in range(0, 10):
            if c ** 3 + d ** 3 + u ** 3 == c * 100 + d * 10 + u:
                print c,d,u
print
print "-" * 40
print

#Desafio 4.1
print "Números de Armstrong:"
print
A = 0
while A <= 999:
    if (A/100) ** 3 + ((A%100)/10) ** 3 + (((A%100)%10)) ** 3 == A:
        print A
    A += 1
print
