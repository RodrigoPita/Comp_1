# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 1
def INVERTER(a):
    L = []
    b = ""
    for k in range(len(a) - 1, -1, -1):
        L.append(a[k])
    return b.join(L)
a = raw_input("Digite uma palavra: ")
print INVERTER(a)

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 2
def PALINDROMO(N):
    L = []
    for a in N:
        Lx = []
        b = ""
        for k in range(len(a) - 1, -1, -1):
            Lx.append(a[k])
        if b.join(Lx) == a:
            L.append(a)
    return L
N = ["ABC", "ABA", "1331", "LOL", "CBD"]
print PALINDROMO(N)

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex 3
import fileinput
def PALAVRAS(N):
    L = []
    for k in N:
        k = k.strip()
        if k not in L:
            L.append(k)
    return L
N = fileinput.input("Palavras/Texto.txt")
print PALAVRAS(N)

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex 4
def EHPRIMO(N):
    x = True
    for k in range(2, (N/2) + 1):
        if N%k == 0:
            x = "False"
    return x
N = input("Digite um número inteiro: ")
print EHPRIMO(N)

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex 5
import fileinput
import random
def SORTEIO(N):
    L = []
    for k in N:
        k = k.strip()
        if k not in L:
            L.append(k)
    x = random.randint(0, len(L) - 1)
    return L[x]
N = fileinput.input("Palavras/Texto.txt")
print SORTEIO(N)

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex 6
def AVALIA(N):
    P = 0
    G = ["D", "C", "C", "A", "D", "B", "A", "E", "A", "A"]
    for y in range(0, 10):
        if N[y] == G[y] or G[y] == "X":
            P += 1
    return P
N = []
for k in range(1, 11):
    x = raw_input("Digite sua resposta (A, B, C, D, E): ")
    N.append(x)
print AVALIA(N)
    
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex 7
import fileinput
def INTERSECAO(M, N):
    L = []
    L1 = []
    L2 = []
    for x in M:
        x = x.strip()
        if x not in L1:
            L1.append(x)
    for y in N:
        y = y.strip()
        if y not in L2:
            L2.append(y)
    for z in range(0, len(L1) - 1):
        for w in range(0, len(L2) - 1):
            if L2[w] == L1[z]:
                L.append(L2[w])
    return L
M = fileinput.input("Palavras/Texto.txt") 
N = fileinput.input("Palavras/Texto2.txt")
print INTERSECAO(M, N)
    
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex 8
import fileinput
def UNIAO(M, N):
    L = []
    L1 = []
    L2 = []
    for x in M:
        x = x.strip()
        if x not in L1:
            L1.append(x)
    for y in N:
        y = y.strip()
        if y not in L2:
            L2.append(y)
    for z in L1:
        L.append(z)
    for w in L2:
        if w not in L:
            L.append(w)
    return L
M = fileinput.input("Palavras/Texto.txt") 
N = fileinput.input("Palavras/Texto2.txt")
print UNIAO(M, N)
    
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex 9
import fileinput
def DIFERENCA(M, N):
    L = []
    L1 = []
    L2 = []
    for x in M:
        x = x.strip()
        if x not in L1:
            L1.append(x)
    for y in N:
        y = y.strip()
        if y not in L2:
            L2.append(y)
    for z in range(0, len(L1) - 1):
        for w in range(0, len(L2) - 1):
            if L2[w] == L1[z]:
                L.append(L2[w])
    for k in L:
        L1.remove(k)
    return L1
M = fileinput.input("Palavras/Texto.txt") 
N = fileinput.input("Palavras/Texto2.txt")
print DIFERENCA(M, N)
    
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex 10
import fileinput
def DOISARQUIVOS(M, N):
    L = []
    L1 = []
    L2 = []
    for x in M:
        x = x.strip()
        if x not in L1:
            L1.append(x)
    for y in N:
        y = y.strip()
        if y not in L2:
            L2.append(y)
    for z in range(0, len(L1) - 1):
        for w in range(0, len(L2) - 1):
            if L2[w] == L1[z]:
                L.append(L2[w])
    text = open("Intersec.txt", "w")
    for l in L:
        text.write(l)
        text.write(" ")
    text.close()
    text = open("Intersec.txt", "r")
    return text.read()
M = fileinput.input("Palavras/Texto.txt") 
N = fileinput.input("Palavras/Texto2.txt")
print DOISARQUIVOS(M, N)
