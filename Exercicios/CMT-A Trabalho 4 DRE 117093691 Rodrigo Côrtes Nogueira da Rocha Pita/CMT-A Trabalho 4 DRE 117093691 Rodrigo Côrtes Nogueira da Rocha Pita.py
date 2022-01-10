# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 1
#Desafio 1.1
import random
resposta = "S"
print "Jogando o Dado"
while resposta == "S":
    print random.randint(1,6)
    resposta = raw_input("Para jogar de novo, aperte 'S': ")
print
print "-" * 40
print
#Desafio 1.2
import random
resposta = "S"
print "Dado de 10 lados"
while resposta == "S":
    print random.randint(1,10)
    resposta = raw_input("Para jogar de novo, aperte 'S': ")
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 2
import random
print "Advinhe o número sorteado entre 1 e 100"
print
print "Para jogar bem, sua pontuação não pode passar de 7"
print
x = -1
min = 1
max = 100
sorteado = random.randint(min, max)
score = 0
while x != sorteado:
    x = input("Digite seu palpite: ")
    if x < min or x > max:
        print
        print "Pensa bem, anta!"
        score = score * 2
        print
    if x > sorteado:
        print "Escolha um número menor!"
        max = x - 1
        score += 1
        print "Pontos: ", score
    elif x < sorteado:
        print "Escolha um número maior!"
        min = x - 1
        score += 1
        print "Pontos: ", score
    else:
        score += 1
        print "Pontos: ", score
        if score <= 7:
            print "Acertou!"
        else:
            print "Jogou mal..."
    print
print "-" * 40
print
#Desafio 2.3
import random
min = input("Digite o número mínimo: ")
max = input("Digite o número máximo: ")
z = random.randint(min, max)
print
print "Adivinhe o número sorteado entre ", min, " e ", max
print
x = input("Digite seu palpite: ")
print
print
while x != z:
    while x < z:
        if x < min:
            print "Pensa bem, anta!"
            print
        min = x + 1
        print "Escolha um número maior"
        x = input("Digite seu palpite: ")
        print
        print
    while x > z:
        if x > max:
            print "Pensa bem, anta!"
            print
        max = x - 1
        print "Escolha um número menor"
        x = input("Digite seu palpite: ")
        print
print "Parabéns, você ganhou!!!"
print
print "-" * 40
print

#Ultra desafio 2 (Você escolhe um número e o PC descobre)
x = y = 50.0
min = 1
max = 100
print "Pense em um número entre 1 e 100"
print
print "Responda 'S', '<' ou '>'"
print
z = raw_input("Aperte 'enter' quando estiver pronto")
print "Você está pensando no número ", x, "?"
resposta = raw_input("")
while resposta != "S":
    while resposta == ">":
        if y > 1:
            y = y/2
            if y == 12.5:
                y = 13
            if y == 7.5:
                y = 8
            if y == 3:
                y = 4
            if y == 1.5:
                y = 2
            x = x + y
            print "Você está pensando no número ", x, "?"
            resposta = raw_input("")
            print
        else:
            x = x + y
            print "Você está pensando no número ", x, "?"
            resposta = raw_input("")
            print
    while resposta == "<":
        if y > 1:
            y = y/2
            if y == 12.5:
                y = 12
            if y == 3:
                y = 3.0
            if y == 1.5:
                y = 2
            x = x - y
            print "Você está pensando no número ", x, "?"
            resposta = raw_input("")
            print
        else:
            x = x - y
            print "Você está pensando no número ", x, "?"
            resposta = raw_input("")
            print
print "Seu número é ", x
print
print "-" * 40
print

#Ultra desafio 2.1 (PC escolhe um número e descobre ele)
import random
x = y = 50.0
min = 1
max = 100
sorteado = random.randint(min, max)
print "Pense em um número entre 1 e 100"
print
print "Responda 'S', '<' ou '>'"
print
print "Você está pensando no número", x, "certo?"
while x != sorteado:
    if x < sorteado:
        print ">"
        print
        if y > 1:
            y = y/2
            if y == 12.5:
                y = 13
            if y == 7.5:
                y = 8
            if y == 3:
                y = 4
            if y == 1.5:
                y = 2
            x = x + y
            print "Você está pensando no número", x, "certo?"
        else:
            x = x + y
            print "Você está pensando no número", x, "certo?"
        max = x - 1
    elif x > sorteado:
        print "<"
        print
        if y > 1:
            y = y/2
            if y == 12.5:
                y = 12
            if y == 3:
                y = 3.0
            if y == 1.5:
                y = 2
            x = x - y
            print "Você está pensando no número", x, "certo?"
        else:
            x = x - y
            print "Você está pensando no número", x, "certo?"
        min = x + 1
print "S"
print
print "Seu número é ", x
