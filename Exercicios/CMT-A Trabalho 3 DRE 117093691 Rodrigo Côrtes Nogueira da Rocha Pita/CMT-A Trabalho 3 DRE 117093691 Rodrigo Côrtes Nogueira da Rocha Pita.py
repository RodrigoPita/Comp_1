# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 1
print "Reta horizontal:"
print "*" * 20
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 2
x = 1
print "Retângulo:"
while x <= 20:
    print "*" * 20
    x += 1
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 3
x = 1
print "Triângulo:"
while x <= 20:
    print "*" * (x) 
    x += 1
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 4
x = 0
print "Triângulo invertido:"
while x <= 20:
    print "*" * (20 - x)
    x += 1
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 5
x = 0
print "Diagonal:"
while x <= 19:
    print " " * (x) + "*"
    x += 1
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 6
x = 0
print "Árvore de Natal com pé:"
while x <= 19:
    print " " * (19 - x) + "*" + "*" * 2 * (x)
    x += 1
while 19 < x <= 22:
    print " " * 13 + "*" * 13
    x += 1
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 7
x = 0
print "Losango:"
while x <= 15:
    print " " * (15 - x) + "*" + "*" * 2 * (x)
    x += 1
while 15 < x <= 30:
    print " " * (x - 15) + "*" + "*" * 2 * (30 - x)
    x += 1
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 8
x = 0
print "Invenção:"
print "* " * 22
while x <= 5:
    while x <= 4:   
        print "*" + " " + " " * 2 * (4 - x) + "*" + "*" + "*" * 4 * (x + 5) + "*" +  " " + " " * 2 * (4 - x) + "*"
        x += 1
    while x <= 5:
        print " " * 2 * (5 - x) + "*" + "*" + "*" * 4 * (x + 5) + "*"
        x += 1
while 5 < x <= 13:
    while x <= 6:    
        print "*" + "*" * 11 + " " * 19 + "*" * 11 + "*"
        x += 1
    while x <= 12:
        while x <= 8:
            print "*" + "*" * 11 + " " * 3 + "*" * 13 + " " * 3 + "*" * 11 + "*"
            x += 1
        while x <= 10:
            print "*" + "*" * 11 + " " * 6 + "*" * 2 + " " * 3 + "*" * 2 + " " * 6 + "*" * 11 + "*"
            x += 1
        while x <= 12:
            print "*" + "*" * 11 + " " * 3 + "*" * 13 + " " * 3 + "*" * 11 + "*"
            x += 1            
    while x <= 13:
        print "*" + "*" * 11 + " " * 19 + "*" * 11 + "*"
        x += 1     
while 13 < x <= 18:  
      print "*" + " " + " " * 2 * (x - 14) + "*" + "*" * 21 + "*" * 4 * (18 - x) + "*" + " " + " " * 2 * (x - 14) + "*"
      x += 1
print "* " * 22
print
print "Fim"





