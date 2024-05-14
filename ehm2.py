from random import randint

def main():
    ...


def sucet(retazec):
    sucet = 0
    while "+" in retazec:
        plus = retazec.find("+")
        sucet += int(retazec[:plus])
        retazec = retazec[plus+1:]
    sucet += int(retazec)
    return sucet

def postupnost1(start, koniec):
    string = ""
    for i in range(start, koniec):
        string += str(i) + " "
    return string[:-1]

def postupnost2(start, koniec, skok=1):
    string = ""
    for i in range(start, koniec, skok):
        string += str(i) + " "
    return string[:-1]

def rozsekaj(text, sirka):
    new = ""
    for i in range(0, len(text), sirka):
        new += f"{text[i:i+sirka]}\n"
    return new

def stvorec(n, znak):
    return f"{znak*n}\n" + f"{znak}{" "*(n-2)}{znak}\n"*(n-2) + f"{znak*n}\n"

def vyhod_duplikaty(retazec):
    new = ""
    for i, j in enumerate(retazec):
        if j != retazec[i-1]:
            new += j
    return new

def ozatvorkuj(retazec, podretazec):
    # new = ""
    # while podretazec in retazec:
    #     kde = retazec.find(podretazec)
    #     new += retazec[:kde] + f"({retazec[kde:kde+len(podretazec)]})"
    #     retazec = retazec[kde+len(podretazec):]
    # new += retazec
    # return new
    return retazec.replace(podretazec, f"({podretazec})")

def prevrat(retazec):
    vysl = ''
    for znak in retazec:
        vysl = znak + vysl
    return vysl

def male(retazec, i):
    hm = ord(retazec[i])
    if ord("A") <= hm <= ord("Z"):
        return retazec[:i] + chr(hm+32) + retazec[i+1:]

def velke(retazec, i):
    hm = ord(retazec[i])
    if ord("a") <= hm <= ord("z"):
        return retazec[:i] + chr(hm-32) + retazec[i+1:]

def riadky(retazec):
    retazec += " "
    for i in range(retazec.count("\n")+1):
        print(f"{i+1}.{retazec[:retazec.find(f"\n")]}")
        retazec = retazec[retazec.find(f"\n")+1:]

def posun_znak(znak, posun):
    hmm = ord(znak)
    if ord("a") <= hmm <= ord("z"):
        hmm += posun
        if hmm > ord("z"):
            hmm -= 26
        if hmm < ord("a"):
            hmm += 26
        return chr(hmm)
    return znak

def zakoduj(text, posun):
    new = ""
    for ch in text:
        new += posun_znak(ch, posun)
    return new

def je_palindrom(retazec):
    opak = ""
    retazec2 = ""
    for i in retazec.lower():
        if i == " ":
            continue
        opak = i + opak
        retazec2 += i
    if opak == retazec2:
        return True
    return False

def usporiadaj(h1, h2, h3):
    if h1 > h2:
        h1, h2 = h2, h1
    if h2 > h3:
        h2, h3 = h3, h2
    if h1 > h2:
        h1, h2 = h2, h1
    return f'{h1} {h2} {h3}'

def nazov(n):
    let1, let2 = chr(randint(ord("a"), ord("z"))), chr(randint(ord("a"), ord("z")))
    while let1 == let2:
        let2 = chr(randint(ord("a"), ord("z")))
    return let1.upper() + let2*n + let1



main()

# a = "Monty Python"
#
# print(a[1:4])
