# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 3
import fileinput
import random
print ("Forca")
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
print ("  _____")
for j in range(1, 6):
    if j == 1:
        print ("  |   |")
    elif j == 2:
        if erro < 1:
            print ("  |   ")
        else:
            print ("  |   O")
    elif j == 3:
        if erro < 2:
            print ("  |  ")
        elif 2 <= erro < 3:
            print ("  |   |")
        elif 3 <= erro < 4:
            print ("  |  -|")
        elif erro >= 4:
            print ("  |  -|-")
    elif j == 4:
        if erro < 5:
            print ("  |   ")
        else:
            print ("  |   |")
    elif j == 5:
        if erro < 6:
            print ("  |  ")
        elif 6 <= erro < 7:
            print ("  |  /")
        elif 7 <= erro < 8:
            print ("  |  /", end = ' ')
            for x in fileinput.input("Palavras/teste.txt"):
                print (x)
        elif 8 <= erro < 9:
            print ("  | _/", end = ' ')
            for x in fileinput.input("Palavras/teste.txt"):
                print (x)
        else:
            print ("  | _/", end = ' ')
            for x in fileinput.input("Palavras/teste.txt"):
                print (x + "_")
print ("__|_____", end = ' ')
for e in range(0, len(Lc)):
    print (Lc[e], end = ' ')
print()
while Lc != Ls:
    if erro <= 9:
        f = (input("Escolha uma letra: ")).upper()
        if f in b:
            print ("Letras erradas:", end = ' ')
            for m in range(0, len(Ll)):
                print (Ll[m], "-", end = ' ')
            for g in range(0, len(b)):
                if f == b[g]:
                    Lc[g] = f
            print()
            print ("  _____")
            for j in range(1, 6):
                if j == 1:
                    print ("  |   |")
                elif j == 2:
                    if erro < 1:
                        print ("  |   ")
                    else:
                        print ("  |   O")
                elif j == 3:
                    if erro < 2:
                        print ("  |  ")
                    elif 2 <= erro < 3:
                        print ("  |   |")
                    elif 3 <= erro < 4:
                        print ("  |  -|")
                    elif erro >= 4:
                        print ("  |  -|-")
                elif j == 4:
                    if erro < 5:
                        print ("  |   ")
                    else:
                        print ("  |   |")
                elif j == 5:
                    if erro < 6:
                        print ("  |  ")
                    elif 6 <= erro < 7:
                        print ("  |  /")
                    elif 7 <= erro < 8:
                        print ("  |  /", end = ' ')
                        for x in fileinput.input("Palavras/teste.txt"):
                            print (x)
                    elif 8 <= erro < 9:
                        print ("  | _/", end = ' ')
                        for x in fileinput.input("Palavras/teste.txt"):
                            print (x)
                    else:
                        print ("  | _/", end = ' ')
                        for x in fileinput.input("Palavras/teste.txt"):
                            print (x + "_")
            print ("__|_____", end = '  ')
            for h in range(0, len(b)):
                print (Lc[h], end = ' ')
            print()
        else:
            if f not in Ll:
                Ll.append(f)
            print ("Letras erradas:", end = ' ')
            for k in range(0, len(Ll)):
                print (Ll[k], "-", end = ' ')
            erro += 1
            print()
            print ("  _____")
            for j in range(1, 6):
                if j == 1:
                    print ("  |   |")
                elif j == 2:
                    if erro < 1:
                        print ("  |   ")
                    else:
                        print ("  |   O")
                elif j == 3:
                    if erro < 2:
                        print ("  |  ")
                    elif 2 <= erro < 3:
                        print ("  |   |")
                    elif 3 <= erro < 4:
                        print ("  |  -|")
                    elif erro >= 4:
                        print ("  |  -|-")
                elif j == 4:
                    if erro < 5:
                        print ("  |   ")
                    else:
                        print ("  |   |")
                elif j == 5:
                    if erro < 6:
                        print ("  |  ")
                    elif 6 <= erro < 7:
                        print ("  |  /")
                    elif 7 <= erro < 8:
                        print ("  |  /", end = ' ')
                        for x in fileinput.input("Palavras/teste.txt"):
                            print (x)
                    elif 8 <= erro < 9:
                        print ("  | _/", end = ' ')
                        for x in fileinput.input("Palavras/teste.txt"):
                            print (x)
                    else:
                        print ("  | _/", end = ' ')
                        for x in fileinput.input("Palavras/teste.txt"):
                            print (x + "_")
            print ("__|_____", end = ' ')
            for i in range(0, len(b)):
                print (Lc[i], end = ' ')
            print()
        print()
        print ("Erros:", erro)
        print()
    else:
        Lc = Ls
if erro <= 9:
    print ("Boa!")
else:
    print ("Jogou mal! A palavra era:", b + ".")
