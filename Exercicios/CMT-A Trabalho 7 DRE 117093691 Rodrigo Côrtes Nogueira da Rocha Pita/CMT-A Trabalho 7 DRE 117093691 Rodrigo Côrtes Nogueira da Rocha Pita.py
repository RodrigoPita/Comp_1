# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 1
import fileinput
import locale
print "Ocorrência dos números na MegaSena:"
print
C = [0] * 61
for x in fileinput.input("Resultado/mega.cvc"):
    x = x.strio()
    L = x.split(";")
    for k in L:
        C[int(k)] + = 1
ma = 0
for y in range(1, 61):
    print y, locale.format('%2d', C[y])
    if C[y] > ma:
        ma = C[y]
        mf = y
print
print mf, locale.format('%2d', ma)
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 2
import fileinput
print "Teste de resultados:"
J = []
for x in range(1, 7):
    if x == 1:
        J.append(input("Digite um número de 1 à 60: "))
    else:
        J.append(input("Digite outro número de 1 à 60: "))
print J
for k in fileinput.input("Resultado/mega.cvc"):
    k = k.strip()
    L = k.split(";")
    C = 0
    for y in J:
        for k in L:
            if y == 4:
                print "Quadra!"
            elif y == 5:
                print "Quina!"
            elif y == 6:
                print "MEGASENA!!!!!"
            
