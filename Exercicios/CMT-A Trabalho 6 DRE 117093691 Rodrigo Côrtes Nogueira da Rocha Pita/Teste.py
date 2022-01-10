#Ex. 3
import fileinput
import random
print "Forca"
print
L = []
Ls = []
Lc = []
for a in fileinput.input("Palavras/Palavras.txt"):
    a = a.strip()
    if a not in L:
        if len(a) >= 10:
            L.append(a)
s = random.randint(0, len(L)-1)
b = L[s]
for k in L[s]:
    Ls.append(k)
c = "*" * len(b)
for d in c:
    Lc.append(d)
erro = 0
for e in range(0, len(Lc)):
    print Lc[e],
print
while Lc != Ls:
    if erro <= 9:
        f = raw_input("Escolha uma letra: ")
        if f in b:
            for g in range(0, len(b)):
                if f == b[g]:
                    Lc[g] = f
            print           
            for h in range(0, len(b)):
                print Lc[h],
            print
        else:
            erro += 1
            print 
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
