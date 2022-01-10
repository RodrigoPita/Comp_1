#Teste - criptografia - Comp. I

def criptografa(S):
    alfabeto=" ?ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    R = ""
    for i in range(0,len(S)):
        if S[i] in alfabeto:
            k = alfabeto.index(S[i])
            R = R + alfabeto[(k+1) % len(alfabeto)]
        else:
            R = R + S[i]
    return (R)

def descriptografa(S):
    alfabeto=" ?ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    R = ""
    for i in range(0,len(S)):
        if S[i] in alfabeto:
            k = alfabeto.index(S[i])
            R = R + alfabeto[(k-1) % len(alfabeto)]
        else:
            R = R + S[i]
    return (R)
S = raw_input ("Entre com uma mensagem: ")

print "Mensagem criptografada:"
R = criptografa(S)
print R

S = raw_input ("Entre com uma mensagem criptografada: ")

print "Mensagem descriptografada:"
R = descriptografa(S)
print R

Fim = input("Fim")
