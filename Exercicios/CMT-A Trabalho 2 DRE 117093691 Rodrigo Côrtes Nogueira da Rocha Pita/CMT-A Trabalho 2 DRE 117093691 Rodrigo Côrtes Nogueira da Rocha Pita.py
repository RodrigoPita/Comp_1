# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo C�rtes Nogueira da Rocha Pita

#Ex. 1

print "Encontrando o maior n�mero"
print ""
a, b, c = input("Digite tr�s n�meros: ")

if a >= b:
    if a >= c:
        print "O maior n�mero � ", a
    else:
        print "O maior n�mero � ", c
elif b >= c:
    print "O maior n�mero � ", b
else:
    print "O maior n�mero � ", c   

#DRE: 117093691
#Rodrigo C�rtes Nogueira da Rocha Pita
    
#Ex. 2
print ""
print ""
print "Encontrando o MDC"
print ""
import locale

a, b = input("Digite dois n�meros: ")
p = 1
print "Passo", " ", "a", " ","b",    "Opera��o"
while a != b:

    if a > b:
        a = a - b
        if p < 10:
            if a < 10:
                print "  ", p, " ", a, "  ", b, "", "a - b"
            else:
                print "  ", p, " ", a, " ", b, "", "a - b"
        else:
            if a < 10:
                print " ", p, " ", a, "  ", b, "", "a - b"
            else:
                print " ", p, " ", a, " ", b, "", "a - b"
        
    else:
        b = b - a
        if p < 10:
            if a < 10:
                print "  ", p, " ", a, "  ", b, "", "b - a"
            else:
                print "  ", p, " ", a, " ", b, "", "b - a"                
        else:
            if a < 10:
                print " ", p, " ", a, "  ", b, "", "b - a"
            else:
                print " ", p, " ", a, " ", b, "", "b - a"
    p = p + 1
print ""
print "MDC = ", a

#DRE: 117093691
#Rodrigo C�rtes Nogueira da Rocha Pita

#Ex. 3
print ""
print ""
print "Tabela das raizes quadradas"
print ""
import math
import locale

a = 2
##print locale.format('%4d', a)
while a <= 10:
    print a, math.sqrt(a)
    a = a + 1
print ""
print ""
print "The End"
