# -*- coding: iso-8859-15 -*-
#BCMT 2017.1 - Turma A - Comp. I
#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 1
print "Calculando a soma dos N primeiros números da série:"
print
def serie(N):
    S = 0
    F = 1
    for k in range (1, N + 1):
        S += F * (1.0/k**2)
        F *= -1
    return S
N = input("Insira o valor de 'N': ")
print serie(N)
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 2
import math
import locale
p = math.pi
print "Aproximando o valor de pi:"
print "Pi =", p
def pi(N):
    S = 0
    F = 1
    for x in range(1, N + 1):
        S += F * (1.0/x**2)
        F *= -1
    Pi = math.sqrt(12.0 * S)
    return Pi

print " " * 3, "Termos", " " * 3, "Val calculado", " " * 3, "Diferença"
for k in range (0, 7):
    D = p - pi(10 ** k)
    print locale.format('%10d', (10**k)), locale.format('%16.9f', pi(10**k)), locale.format('%15.9f', D)
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 3
print "Calculando o MDC de dois números:"
print
def MDC(x, y):
    while x != y:
        if x > y:
            x -= y
        if y > x:
            y -= x
    MDC = x
    return MDC
x, y = input("Digite os dois números: ")
print MDC(x, y)
print
print "-" * 40
print

#DRE: 117093691
#Rodrigo Côrtes Nogueira da Rocha Pita

#Ex. 4
print "Calculando o fatorial de um número inteiro N:"
print
def fat(N):
    F = 1
    for k in range(1, N + 1):
        F *= k
    return F
N = input("Digite o número 'N': ")
print fat(N)
