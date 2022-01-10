print "Calculando quantos dias voce tem de vida"
print
dh = input("Digite o dia de hoje: ")
mh = input("Digite o mes atual: ")
ah = input("Digite o ano atual: ")
print
dv = 0
dn = input("Digite o dia em que voce nasceu: ")
mn = input("Digite o mes em que voce nasceu: ")
an = input("Digite o ano em que voce nasceu: ")
print
for a in range(an, an + 1):
    for m in range(mn, mn + 1):
        if m == 4 or m == 6 or m == 9 or m == 11:
            ds = 30
        elif m == 2:
            if a % 4 == 0 or a % 400 == 0:
                ds = 29
            else:
                ds = 28
        else:
            ds = 31
        for d in range(dn, ds + 1):
            dv += 1
    for m in range(mn + 1, 13):
        if m == 4 or m == 6 or m == 9 or m == 11:
            ds = 30
        elif m == 2:
            if a % 4 == 0 or a % 400 == 0:
                ds = 29
            else:
                ds = 28
        else:
            ds = 31
        for d in range(1, ds + 1):
            dv += 1
for a in range(an + 1, ah):
    for m in range(1, 13):
        if m == 4 or m == 6 or m == 9 or m == 11:
            ds = 30
        elif m == 2:
            if a % 4 == 0 or a % 400 == 0:
                ds = 29
            else:
                ds = 28
        else:
            ds = 31
        for d in range(1, ds + 1):
            dv += 1
for a in range(ah, ah + 1):
    for m in range(1, mh):
        if m == 4 or m == 6 or m == 9 or m == 11:
            ds = 30
        elif m == 2:
            if a % 4 == 0 or a % 400 == 0:
                ds = 29
            else:
                ds = 28
        else:
            ds = 31
        for d in range(1, ds + 1):
            dv += 1
    for m in range(mh, mh + 1):
        if m == 4 or m == 6 or m == 9 or m == 11:
            ds = 30
        elif m == 2:
            if a % 4 == 0 or a % 400 == 0:
                ds = 29
            else:
                ds = 28
        else:
            ds = 31
        for d in range(1, dh + 1):
            dv += 1
print "Voce tem", dv - 2, "dias de vida"

