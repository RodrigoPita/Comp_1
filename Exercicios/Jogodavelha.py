# -*- coding: iso-8859-15 -*-
import random
print "Jogo da Velha:"
print
##for x in range(1, 31):
##    if x == 10 or x == 20:
##        print "* " * 29 + "*"
##    else:
##        print " " * 19 + "*" + " " * 19 + "*"
##print

###Circulo
##for k in range(2, 9):
##    if k == 2 or k == 8:
##        print " " * 5 + "# " + "#"
##    if k == 3 or k == 7:
##        print " " * 2 + "#" + " " * 7 + "#"
##    if k == 4 or k == 5 or k == 6:
##        print " #" +" " * 9 + "#"
##
###X (4 espaços horizontais e 1 vertical)
##for l in range(2, 5):
##    print " " + " " * 2 * (l - 2) + "#",
##    print " " * 4 * (4 - l) + "#"
##    
##for l in range(2, 5):
##    print " " + " " * 2 * (4 - l) + "#",
##    print " " * 4 * (l - 2) + "#"

a = raw_input("Insira o Quadrante (Q1 à Q9): ")
        
for x in range(1, 11):
    if a == "Q1":
        if x == 2 or x == 8:
            print " " * 3 + " " * 5 + "# # " + "#" + " " * 6 + "*" + " " * 19 + "*"
        elif x == 3 or x == 7:
            print " " * 4 + " " * 2 + "#" + " " * 7 + "#"
        elif x == 4 or x == 5 or x == 6:
            print " " * 4 + " #" +" " * 9 + "#"
    if x == 10:
        print "* " * 29 + "*"
    else:
        print " " * 19 + "*" + " " * 19 + "*"
print








