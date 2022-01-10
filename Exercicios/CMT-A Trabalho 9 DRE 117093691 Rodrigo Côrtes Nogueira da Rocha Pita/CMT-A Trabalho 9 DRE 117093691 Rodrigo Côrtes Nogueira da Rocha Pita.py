# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 1
import fileinput
P = []
print "Listando palavras de um arquivo:"
print
for k in fileinput.input("Textos/javanes.txt"):
    k = k.strip()
    L = k.split(" ")
    for x in L:
        x = x.replace(",", "")
        x = x.replace(".", "")
        x = x.replace(":", "")
        x = x.replace(";", "")
        x = x.replace("!", "")
        x = x.replace("?", "")
        if len(x) >= 4:
            if x not in P:
                P.append(x)
            P.sort()    
for y in P:
    print y
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 2
import locale
import fileinput
P = []
C = []
print "Contando o número de ocorrência das palavras:"
print
for k in fileinput.input("Textos/javanes.txt"):
    k = k.strip()
    L = k.split(" ")
    for x in L:
        x = x.replace(",", "")
        x = x.replace(".", "")
        x = x.replace(":", "")
        x = x.replace(";", "")
        x = x.replace("!", "")
        x = x.replace("?", "")
        if len(x) >= 4:
            if x not in P:
                P.append(x)
                C.append(1)
            else:
                p = P.index(x)
                C[p] += 1
            P.sort()    
for y in range(0, len(P)):
    print P[y], C[y]
