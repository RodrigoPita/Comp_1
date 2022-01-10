import random
import locale
B = ["J", "Q", "K", "A"] * 4
J1 = []
J1c = []
J2 = []
J2c = []
J3 = []
J3c = []
J4 = []
J4c = []
JC = []
JCc = []
for k in range(2, 10):
    B.append(k)
    B.append(k)
    B.append(k)
    B.append(k)
random.shuffle(B)

#Cartas
def Cartas(N):
    for x in range(1, 6):
        if N == "J" or N == "Q" or N == "K" or N == "A":
            if x == 1 or x == 5:
                print "-" * 6
            if x == 2:
                print "|" + (N) + "   |"            
            elif x == 3:
                print "|    |"
            elif x == 4:
                print "|   " + (N) + "|"
        else:
            if x == 1 or x == 5:
                print "-" * 6
            elif x == 4:
                print "|", locale.format('%3d', N) + "|"
            elif x == 2: 
                if C == 10:
                    print "|" + locale.format('%d', N) + "  |" 
                else:
                    print "|" + str(N) + "   |" 
            else:
                print "|    |"
    return ""
a = input("Quantos jogadores? ")
print
if a == 1:
    b = input("Jogador 1: Quanto deseja apostar? ")
    print
    print "Cartas do Jogador 1"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        print Cartas(C)
        J1c.append(C)
        if C == "J" or C == "Q" or C == "K":
            J1.append(10)
        elif C == "A":
            J1.append(11)
        else:  
            J1.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Croupier"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        print Cartas(C)
        JCc.append(C)
        if C == "J" or C == "Q" or C == "K":
            JC.append(10)
        elif C == "A":
            JC.append(11)
        else:  
            JC.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print
    print "Pontos do Jogador 1"
    PJ1 = J1[0] + J1[1]
    if PJ1 == 22:
        PJ1 = 2
    print PJ1
    print "Pontos do Croupier"
    PJC = JC[0] + JC[1]
    if PJC == 22:
        PJC = 2
    print PJC
    print
    f = raw_input("Jogador 1: Deseja continuar? [S/N] ")
    if f == "S":
        print "Cartas do Jogador 1"
        for j in J1c:
            print Cartas(j)
        C = B[0]
        print Cartas(C)
        J1c.append(C)
        if C == "J" or C == "Q" or C == "K":
            J1.append(10)
        elif C == "A":
            J1.append(11)
        else:  
            J1.append(C)
        B.remove(C)
        print
        print "Cartas do Croupier"
        if PJC > 16:
            for l in JCc:
                print Cartas(l)
        else:
            for l in JCc:
                print Cartas(l)
            C = B[0]
            print Cartas(C)
            JCc.append(C)
            if C == "J" or C == "Q" or C == "K":
                JC.append(10)
            elif C == "A":
                JC.append(11)
            else:  
                JC.append(C)
            B.remove(C)
        print "Pontos do Jogador 1"
        PJ1 += J1[2]
        if PJ1 == 22:
            PJ1 = 2
        print PJ1
        print "Pontos do Croupier"
        if PJC > 16:
            PJC = JC[0] + JC[1]
            if PJC == 22:
                PJC = 2
        else:
            PJC += JC[2]
        print PJC
        print    
if a == 2:
    b = input("Jogador 1: Quanto deseja apostar? ")
    c = input("Jogador 2: Quanto deseja apostar? ")
    print
    print "Cartas do Jogador 1"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            J1.append(10)
        elif C == "A":
            J1.append(11)
        else:  
            J1.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Jogador 2"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            J2.append(10)
        elif C == "A":
            J2.append(11)
        else:  
            J2.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Croupier"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            JC.append(10)
        elif C == "A":
            JC.append(11)
        else:  
            JC.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print
    print "Pontos do Jogador 1"
    PJ1 = J1[0] + J1[1]
    print PJ1
    print "Pontos do Jogador 2"
    PJ2 = J2[0] + J2[1]
    print PJ2
    print "Pontos do Croupier"
    PJC = JC[0] + JC[1]
    print PJC
    print
if a == 3:
    b = input("Jogador 1: Quanto deseja apostar? ")
    c = input("Jogador 2: Quanto deseja apostar? ")
    d = input("Jogador 3: Quanto deseja apostar? ")
    print
    print "Cartas do Jogador 1"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            J1.append(10)
        elif C == "A":
            J1.append(11)
        else:  
            J1.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Jogador 2"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            J2.append(10)
        elif C == "A":
            J2.append(11)
        else:  
            J2.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Jogador 3"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            J3.append(10)
        elif C == "A":
            J3.append(11)
        else:  
            J3.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Croupier"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            JC.append(10)
        elif C == "A":
            JC.append(11)
        else:  
            JC.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print
    print "Pontos do Jogador 1"
    PJ1 = J1[0] + J1[1]
    print PJ1
    print "Pontos do Jogador 2"
    PJ2 = J2[0] + J2[1]
    print PJ2
    print "Pontos do Jogador 3"
    PJ3 = J3[0] + J3[1]
    print PJ3
    print "Pontos do Croupier"
    PJC = JC[0] + JC[1]
    print PJC
    print
if a == 4:
    b = input("Jogador 1: Quanto deseja apostar? ")
    c = input("Jogador 2: Quanto deseja apostar? ")
    d = input("Jogador 3: Quanto deseja apostar? ")
    e = input("Jogador 4: Quanto deseja apostar? ")
    print
    print "Cartas do Jogador 1"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            J1.append(10)
        elif C == "A":
            J1.append(11)
        else:  
            J1.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Jogador 2"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            J2.append(10)
        elif C == "A":
            J2.append(11)
        else:  
            J2.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Jogador 3"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            J3.append(10)
        elif C == "A":
            J3.append(11)
        else:  
            J3.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Jogador 4"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            J4.append(10)
        elif C == "A":
            J4.append(11)
        else:  
            J4.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print "Cartas do Croupier"
    print
    for x in range(1, 3):
        A = random.randint(0, len(B) - 1)
        C = B[0]
        for x in range(1, 6):
            if C == "J" or C == "Q" or C == "K" or C == "A":
                if x == 1 or x == 5:
                    print "-" * 6
                if x == 2:
                    print "|" + (C) + "   |"            
                elif x == 3:
                    print "|    |"
                elif x == 4:
                    print "|   " + (C) + "|"
            else:
                if x == 1 or x == 5:
                    print "-" * 6
                elif x == 4:
                    print "|", locale.format('%3d', C) + "|"
                elif x == 2: 
                    if C == 10:
                        print "|" + locale.format('%d', C) + "  |" 
                    else:
                        print "|" + str(C) + "   |" 
                else:
                    print "|    |"
        if C == "J" or C == "Q" or C == "K":
            JC.append(10)
        elif C == "A":
            JC.append(11)
        else:  
            JC.append(C)
        B.remove(C)
        print
    w = raw_input("Aperte ENTER para continuar...")
    print
    print "Pontos do Jogador 1"
    PJ1 = J1[0] + J1[1]
    print PJ1
    print "Pontos do Jogador 2"
    PJ2 = J2[0] + J2[1]
    print PJ2
    print "Pontos do Jogador 3"
    PJ3 = J3[0] + J3[1]
    print PJ3
    print "Pontos do Jogador 4"
    PJ4 = J4[0] + J4[1]
    print PJ4
    print "Pontos do Croupier"
    PJC = JC[0] + JC[1]
    print PJC
    print
