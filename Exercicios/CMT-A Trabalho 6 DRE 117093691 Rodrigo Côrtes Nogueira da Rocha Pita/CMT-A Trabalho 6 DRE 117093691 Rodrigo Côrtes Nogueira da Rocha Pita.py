# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 1
import fileinput
L = []
print "Lista:"
print
for x in fileinput.input("Palavras/Texto.txt"):
    x = x.strip()
    if len(x) >= 4:
        if x not in L:
            L.append(x)
        L.sort()
for z in range(0, len(L)):
    print L[z]
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 2
import fileinput
print "Pesquisa de palavras:"
print
P = raw_input("Digite o padrão: ")
for x in fileinput.input("Palavras/Palavras.txt"):
    x = x.strip()
    if len(x) == len(P):
        z = 0
        for y in range(0, len(P)):
            if P[y] == "*":
                z += 1
            elif x[y] == P[y]:
                z += 1
        if z == len(P):
            print x
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 3
import fileinput
import random
print "Forca"
print
L = []
Ls = []
Lc = []
Ll = []
for a in fileinput.input("Palavras/Palavras.txt"):
    a = a.strip()
    if a not in L:
        if len(a) >= 10:
            L.append(a)
s = random.randint(0, len(L)-1)
b = L[s]
for k in L[s]:
    Ls.append(k)
c = "_" * len(b)
for d in c:
    Lc.append(d)
erro = 0
print "  _____"
for j in range(1, 6):
    if j == 1:
        print "  |   |"
    elif j == 2:
        if erro < 1:
            print "  |   "
        else:
            print "  |   O"
    elif j == 3:
        if erro < 2:
            print "  |  "
        elif 2 <= erro < 3:
            print "  |   |"
        elif 3 <= erro < 4:
            print "  |  -|"
        elif erro >= 4:
            print "  |  -|-"
    elif j == 4:
        if erro < 5:
            print "  |   "
        else:
            print "  |   |"
    elif j == 5:
        if erro < 6:
            print "  |  "
        elif 6 <= erro < 7:
            print "  |  /"
        elif 7 <= erro < 8:
            print "  |  /",
            for x in fileinput.input("Palavras/teste.txt"):
                print x
        elif 8 <= erro < 9:
            print "  | _/",
            for x in fileinput.input("Palavras/teste.txt"):
                print x
        else:
            print "  | _/",
            for x in fileinput.input("Palavras/teste.txt"):
                print x + "_"
print "__|_____",
for e in range(0, len(Lc)):
    print Lc[e],
print
while Lc != Ls:
    if erro <= 9:
        f = raw_input("Escolha uma letra: ")
        if f in b:
            print "Letras erradas:",
            for m in range(0, len(Ll)):
                print Ll[m], "-",
            for g in range(0, len(b)):
                if f == b[g]:
                    Lc[g] = f
            print
            print "  _____"
            for j in range(1, 6):
                if j == 1:
                    print "  |   |"
                elif j == 2:
                    if erro < 1:
                        print "  |   "
                    else:
                        print "  |   O"
                elif j == 3:
                    if erro < 2:
                        print "  |  "
                    elif 2 <= erro < 3:
                        print "  |   |"
                    elif 3 <= erro < 4:
                        print "  |  -|"
                    elif erro >= 4:
                        print "  |  -|-"
                elif j == 4:
                    if erro < 5:
                        print "  |   "
                    else:
                        print "  |   |"
                elif j == 5:
                    if erro < 6:
                        print "  |  "
                    elif 6 <= erro < 7:
                        print "  |  /"
                    elif 7 <= erro < 8:
                        print "  |  /",
                        for x in fileinput.input("Palavras/teste.txt"):
                            print x
                    elif 8 <= erro < 9:
                        print "  | _/",
                        for x in fileinput.input("Palavras/teste.txt"):
                            print x
                    else:
                        print "  | _/",
                        for x in fileinput.input("Palavras/teste.txt"):
                            print x + "_"                            
            print "__|_____",           
            for h in range(0, len(b)):
                print Lc[h],
            print
        else:
            if f not in Ll:
                Ll.append(f)
            print "Letras erradas:",
            for k in range(0, len(Ll)):
                print Ll[k], "-",
            erro += 1
            print
            print "  _____"
            for j in range(1, 6):
                if j == 1:
                    print "  |   |"
                elif j == 2:
                    if erro < 1:
                        print "  |   "
                    else:
                        print "  |   O"
                elif j == 3:
                    if erro < 2:
                        print "  |  "
                    elif 2 <= erro < 3:
                        print "  |   |"
                    elif 3 <= erro < 4:
                        print "  |  -|"
                    elif erro >= 4:
                        print "  |  -|-"
                elif j == 4:
                    if erro < 5:
                        print "  |   "
                    else:
                        print "  |   |"
                elif j == 5:
                    if erro < 6:
                        print "  |  "
                    elif 6 <= erro < 7:
                        print "  |  /"
                    elif 7 <= erro < 8:
                        print "  |  /",
                        for x in fileinput.input("Palavras/teste.txt"):
                            print x
                    elif 8 <= erro < 9:
                        print "  | _/",
                        for x in fileinput.input("Palavras/teste.txt"):
                            print x
                    else:
                        print "  | _/",
                        for x in fileinput.input("Palavras/teste.txt"):
                            print x + "_"
            print "__|_____",  
            for i in range(0, len(b)):
                print Lc[i],
            print
        print
        print "Erros:", erro
        print
    else:
        Lc = Ls
if erro <= 9:
    print "Boa!"
else:
    print "Jogou mal! A palavra era:", b + "."
