f_mena = open("menaa.txt", "r", encoding="utf-8")
f_priez = open("priezviska.txt", "r", encoding="utf-8")
f_menapriez = open("mena_priez.txt", "w", encoding="utf-8") #otvori subor na zapis, pripadne vytori novy alebo zname obsah stareho

for meno in f_mena:
    priez = f_priez.readline()
    print(f"{meno.strip()} {priez.strip()}", file=f_menapriez)
    # f_menapriez.write(f"{meno.strip()} {priez.strip()}\n")












f_mena.close()
f_priez.close()
f_menapriez.close()