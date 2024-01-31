def main():
    a = int(input("Zadaj a: "))
    b = int(input("Zadaj b: "))
    its = sucet(a, b)
    print(f"Sucet cisel {a} a {b} je {its}")
    print(f"Cislo {a} je {parne(a)}.")
    print(f"Cislo {b} je {parne(b)}.")
    if prvocislo(a):
        print(f"Cislo {a} je prvocislo.")
    else:
        print(f"Cislo {a} nie je prvocislo.")
    if prvocislo(b):
        print(f"Cislo {b} je prvocislo.")
    else:
        print(f"Cislo {b} nie je prvocislo.")



def sucet(a, b):
    return a + b

def parne(a):
    if a % 2 == 0:
        return "parne "
    else:
        return "neparne"

def prvocislo(a):
    times = 0
    for i in range(1, a+1):
        if a % i == 0:
            times += 1

    if times == 2:
        return True
    else:
        return False


main()